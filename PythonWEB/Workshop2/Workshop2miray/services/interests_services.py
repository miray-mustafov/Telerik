import math
from sqlite3 import IntegrityError

from data.database import insert_query, read_query, update_query
from data.models import INTEREST_INCREASE_PERCENTAGE, INITIAL_INTEREST


def _increase_interest(cur_interest, incr=INTEREST_INCREASE_PERCENTAGE):
    interest = cur_interest + (incr / 100 * cur_interest)
    return math.ceil(interest)


def add_profile_category_pair(profile_id: int, category_id: int) -> bool:
    try:
        insert_query("INSERT INTO interests(category_id, profile_id, relevance) VALUES (?, ?, ?)",
                     (category_id, profile_id, INITIAL_INTEREST))
        return True
    except IntegrityError:
        return False


def update_profile_category_interest(profile_id: int, category_id: int):
    data = read_query(
        f'''SELECT relevance FROM interests WHERE category_id = ? AND profile_id = ?''',
        (category_id, profile_id,)
    )
    interest = _increase_interest(data[0][0])
    update_query(
        f'''UPDATE interests SET relevance = ? WHERE category_id = ? AND profile_id = ?''',
        (interest, category_id, profile_id,)
    )
    return interest


def get_profile_category_interests(profile_id):
    data = read_query(
        f'''SELECT category_id, relevance FROM interests WHERE profile_id = ?''',
        (profile_id,)
    )
    if data:
        return data
