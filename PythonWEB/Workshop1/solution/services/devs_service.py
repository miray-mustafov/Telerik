from data.models import Dev, Project, DevLevelMaps
from data.database import insert_query, read_query, query_count


def get_all(name=None, level=None):
    sql = '''SELECT id, name, level FROM devs'''

    where_clauses = []
    if name:
        where_clauses.append(f"name like '%{name}%'")
    if level:
        where_clauses.append(f"level = {DevLevelMaps.STR_TO_INT[level]}")

    if where_clauses:
        sql += ' WHERE ' + ' AND '.join(where_clauses)

    return (Dev.from_query_result(*row) for row in read_query(sql))


def get_by_id(id: int):
    dev_raw_data = read_query(
        'SELECT id, name, level FROM devs WHERE id = ?', (id,))

    if not dev_raw_data:
        return None

    projects_raw_data = read_query(
        'SELECT id, name, is_open, team_limit FROM projects JOIN devs_projects ON id = project_id WHERE dev_id = ?', (id,))

    return Dev.from_query_result(
        *dev_raw_data[0],
        [Project.from_query_result(*row) for row in projects_raw_data])


def name_exists(name: str):
    return query_count('SELECT COUNT(*) from devs WHERE name = ?', (name,)) > 0


def id_exists(id: int):
    return query_count('SELECT COUNT(*) from devs WHERE id = ?', (id,)) > 0


def create(dev: Dev):
    generated_id = insert_query(
        'INSERT INTO devs(name,level) VALUES(?,?)',
        (dev.name, DevLevelMaps.STR_TO_INT[dev.level]))

    dev.id = generated_id

    return dev
