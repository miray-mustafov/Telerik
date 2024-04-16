from data.models import Project
from data.database import insert_query, read_query, update_query


def all(name=None, limit=None, status=None):
    filters = []
    parameters = []

    if name:
        filters.append(f"name LIKE ?")
        parameters.append(f"%{name}%")
    if limit is not None:
        filters.append(f"team_limit <= ?")
        parameters.append(limit)
    if status:
        is_open = 1 if status.lower() == 'open' else 0
        filters.append(f"is_open = ?")
        parameters.append(is_open)

    query = (f"SELECT id, name, is_open, team_limit FROM projects" +
             (" WHERE " + " AND ".join(filters) if filters else ""))
    data = read_query(query, parameters)
    return data