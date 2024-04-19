from data.models import Dev, Project, DevLevelMaps
from data.database import insert_query, read_query, query_count, update_query


def get_all(name: str = None, limit: int = None, status: str = None):
    sql = '''SELECT id, name, is_open, team_limit FROM projects'''

    where_clauses = []
    if name:
        where_clauses.append(f"name like '%{name}%'")
    if limit:
        where_clauses.append(f"team_limit <= {limit}")
    if status:
        where_clauses.append(f"is_open = {1 if status == 'open' else 0}")

    if where_clauses:
        sql += ' WHERE ' + ' AND '.join(where_clauses)

    return (Project.from_query_result(*row) for row in read_query(sql))


def get_by_id(id: int):
    project_raw_data = read_query(
        'SELECT id, name, is_open, team_limit FROM projects WHERE id = ?', (id,))

    if not project_raw_data:
        return None

    dev_raw_data = read_query(
        'SELECT id, name, level FROM devs JOIN devs_projects ON id = dev_id WHERE project_id = ?', (id,))

    return Project.from_query_result(
        *project_raw_data[0],
        [Dev.from_query_result(*row) for row in dev_raw_data])


def name_exists(name: str):
    return query_count('SELECT COUNT(*) from projects WHERE name = ?', (name,)) > 0


def id_exists(id: int):
    return query_count('SELECT COUNT(*) from projects WHERE id = ?', (id,)) > 0


def create(project: Project):
    generated_id = insert_query(
        'INSERT INTO projects(name,is_open,team_limit) VALUES(?,?,?)',
        (project.name, 1 if project.status == 'open' else 0, project.limit))

    project.id = generated_id

    return project


def set_status(id: int, status: str):
    return update_query(
        'UPDATE projects SET is_open = ? WHERE id = ?',
        (1 if status == 'open' else 0, id))


def assign_to_project(project_id: int, dev_id: int):
    if query_count('''SELECT COUNT(*) FROM devs_projects 
                   WHERE dev_id = ? AND project_id = ?''', (dev_id, project_id)) > 0:
        return False, 'Dev already assigned to project.'

    limit, is_open = read_query('''SELECT team_limit, is_open
                                   FROM projects WHERE id = ?''', (project_id,))[0]
    project_devs_levels = read_query('''SELECT level FROM devs 
                                        JOIN devs_projects ON id = dev_id 
                                        WHERE project_id = ?''', (project_id,))

    devs_count = len(project_devs_levels)

    if not is_open:
        return False, 'Cannot assign to closed projects.'
    if limit == devs_count:
        return False, 'Cannot assign additional devs to full projects.'

    dev_level, dev_projects_count = read_query(
        '''SELECT level, (SELECT COUNT(*) from devs_projects WHERE dev_id = id) 
           FROM devs WHERE id = ?''', (dev_id,))[0]
    
    senior_level = DevLevelMaps.STR_TO_INT['senior']
    has_no_senior = all(level[0] < senior_level for level in project_devs_levels)
    
    if has_no_senior and devs_count + 1 == limit and dev_level < senior_level:
        return False, 'At least one senior must be assigned to a project.'
    if dev_projects_count > 0 and dev_level < senior_level:
        return False, 'Only senior devs can be assigned to more than one project.'

    insert_query('''INSERT INTO devs_projects(dev_id, project_id)
                    VALUES(?,?)''', (dev_id, project_id))

    return True, 'Dev assigned to project.'


def remove_from_project(project_id: int, dev_id: int):
    if query_count('''SELECT COUNT(*) FROM devs_projects 
                   WHERE dev_id = ? AND project_id = ?''', (dev_id, project_id)) == 0:
        return False, 'Dev not assigned to this project.'

    update_query('''DELETE FROM devs_projects 
                    WHERE dev_id = ? AND project_id = ?''', (dev_id, project_id))

    return True, 'Dev removed from project.'
