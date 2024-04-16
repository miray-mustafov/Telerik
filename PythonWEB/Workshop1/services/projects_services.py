from data.models import Project
from data.database import insert_query, read_query, update_query


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
    return data
