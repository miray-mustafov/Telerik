from data.models import Project, DEV_LEVELS
from data.database import insert_query, read_query, update_query


def get_all(name=None, level_str=None):
    filters, params = [], []
    if name:
        filters.append('name LIKE ?')
        params.append(f"%{name}%")
    if level_str:
        filters.append('level = ?')
        params.append(DEV_LEVELS[level_str])

    query = ('SELECT id, name, level FROM devs' +
             (' WHERE ' + ' AND '.join(filters) if filters else ""))
    data = read_query(query, params)
    return data
