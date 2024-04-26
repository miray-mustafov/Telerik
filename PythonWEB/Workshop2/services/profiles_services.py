from data.database import read_query
from data.models import Profile


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
