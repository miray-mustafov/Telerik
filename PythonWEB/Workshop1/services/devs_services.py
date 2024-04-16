from data.models import Developer, DEV_LEVELS, LEVEL_DEVS
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

    devs = [Developer(id=did, name=dname, level_str=LEVEL_DEVS[dlevel]) for did, dname, dlevel in data]
    return devs


def get_by_id(id: int):
    data = read_query('SELECT id,name,level FROM devs WHERE id = ?', (id,))
    # todo here
    return data
