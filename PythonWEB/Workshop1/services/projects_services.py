from data.models import Project
from data.database import insert_query, read_query, update_query


def all(name=None, limit=None, status=None):
    if not any([name, limit, status]):
        query = "SELECT id, name, is_open, team_limit FROM projects"
    else:
        query = "SELECT id, name, is_open, team_limit FROM projects WHERE"
    parameters = []

    if name:
        query += " name LIKE ?"
        parameters.append(f"%{name}%")

    if limit is not None:
        if not name:
            query += " team_limit <= ?"
        else:
            query += " AND team_limit <= ?"
        parameters.append(limit)

    if status:
        is_open = 1 if status.lower() == 'open' else 0
        if not name and not limit:
            query += " is_open = ?"
        else:
            query += " AND is_open = ?"
        parameters.append(is_open)

    data = read_query(query, parameters)
    return data
