from data.database import read_query
from data.models import Profile


def profile_exists(id: int):
    data = read_query('''
        SELECT COUNT(*) FROM profiles WHERE id = ? 
        ''', (id,))
    return data[0][0] > 0


def get_all(country_code: str | None = None) -> list[Profile]:
    query = 'SELECT id, ip_address, country_code FROM profiles'
    params = ()

    if country_code:
        query += ' WHERE country_code = ?'
        params = (country_code,)

    data = read_query(query, params)
    if data:
        data = [Profile(id=id, ip_address=ip, country_code=code) for id, ip, code in data]
    return data


def get_all_country_codes() -> list[str]:
    """
    Takes all unique codes and unpacks the nested lists with one el
    """
    data = read_query('SELECT DISTINCT country_code FROM profiles')
    data = [c[0] for c in data]
    return data


def get_by_id_with_categories(id: int) -> Profile | None:
    data = read_query('''
        SELECT p.id, p.ip_address, p.country_code, c.id, c.name, i.relevance
        FROM profiles AS p
        JOIN interests AS i ON p.id = i.profile_id
        JOIN categories AS c ON i.category_id = c.id
        WHERE i.profile_id = ?
        ''', (id,))

    if not data:
        return None

    data = list(sorted(data, key=lambda x: -x[-1]))
    data = _response_object(data)
    return data


def _response_object(data):
    profile_id = data[0][0]
    ip_address = data[0][1]
    country_code = data[0][2]

    user_categories_with_relevance = []
    for _, _, _, cid, cname, relevance in data:
        user_categories_with_relevance.append({
            'id': cid,
            'name': cname,
            'relevance': relevance,
        })

    return {
        'profile_id': profile_id,
        'ip_address': ip_address,
        'country_code': country_code,
        'categories': user_categories_with_relevance
    }
