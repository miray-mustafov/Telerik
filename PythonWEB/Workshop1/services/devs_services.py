from data.models import Developer, Project, DEV_LEVELS, LEVEL_DEVS
from data.database import insert_query, read_query, update_query
import sqlite3
from pydantic import ValidationError


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

    devs = [Developer(id=did, name=dname, level_str=LEVEL_DEVS[dlevel])
            for did, dname, dlevel in data]
    return devs


def get_by_id(id: int):
    data = read_query('SELECT id,name,level FROM devs WHERE id = ?', (id,))
    if not data:
        return None
    dev = [Developer(id=did, name=dname, level_str=LEVEL_DEVS[dlevel])
           for did, dname, dlevel in data][0]
    return dev


def create(dev: Developer):
    try:
        # todo trigger potential pydantic constr errors from the model
        # new_dev = Developer(name=dev.name, level_str=dev.level_str)

        # To trigger potential db constraint error
        generated_id = insert_query(
            'INSERT INTO devs(name,level) VALUES(?,?)',
            (dev.name, DEV_LEVELS[dev.level_str]))

        dev.id = generated_id
        return dev
    except sqlite3.Error as e:
        return "Error:", e.args[0]

    # except ValidationError as e:
    #     Handle pydantic errors ?


def assign_project(dev: Developer, project: Project):
    return None


def delete(id: int):
    update_query(
        '''DELETE FROM devs WHERE id = ?''', (id,)
    )
