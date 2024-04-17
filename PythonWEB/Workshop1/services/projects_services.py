import sqlite3
from data.models import Project, PROJECT_NUMS_STATUS, PROJECT_STATUS_NUMS, ProjectStatusUpdate
from data.database import insert_query, read_query, update_query


def is_team_limit_reached(project: Project):
    cur_team_count = read_query(
        'SELECT COUNT(*) FROM devs_projects WHERE project_id = ?', (project.id,)
    )
    cur_team_count = cur_team_count[0][0]
    return project.team_limit == cur_team_count


def get_all(name=None, limit=None, status=None):
    filters, params = [], []

    if name:
        filters.append(f"name LIKE ?")
        params.append(f"%{name}%")
    if limit is not None:
        filters.append(f"team_limit <= ?")
        params.append(limit)
    if status:
        is_open = 1 if status.lower() == 'open' else 0
        filters.append(f"is_open = ?")
        params.append(is_open)

    query = (f"SELECT id, name, is_open, team_limit FROM projects" +
             (" WHERE " + " AND ".join(filters) if filters else ""))
    data = read_query(query, params)

    projects = [Project(id=pid, name=pname, status=PROJECT_NUMS_STATUS[pis_open], team_limit=plimit)
                for pid, pname, pis_open, plimit in data]
    return projects


def get_by_id(id: int):
    data = read_query('SELECT id,name,is_open,team_limit FROM projects WHERE id = ?', (id,))
    if not data:
        return None
    project = [Project(id=pid, name=pname, status=PROJECT_NUMS_STATUS[pis_open], team_limit=plimit)
               for pid, pname, pis_open, plimit in data][0]
    return project


def create(project: Project):
    try:
        # To trigger potential db constraint error
        generated_id = insert_query(
            'INSERT INTO projects(name,is_open,team_limit) VALUES(?,?,?)',
            (project.name, PROJECT_STATUS_NUMS[project.status], project.team_limit))

        project.id = generated_id
        return project
    except sqlite3.Error as e:
        return "Error:", e.args[0]


def delete(id: int):
    update_query(
        '''DELETE FROM projects WHERE id = ?''', (id,)
    )


def update(existing_project: Project, status_obj: ProjectStatusUpdate):
    new_is_open = PROJECT_STATUS_NUMS[status_obj.status]
    update_query('UPDATE projects SET is_open = ? WHERE id = ? ',
                 (new_is_open, existing_project.id))

    existing_project.status = status_obj.status
    return existing_project
