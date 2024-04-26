from data.database import read_query
from data.models import CategoryRelevance


def get_all(country_code: str | None):
    if country_code:
        query = '''
            SELECT c.id,
                   c.name,
                   COALESCE(SUM(i.relevance), 0) AS cumulative_relevance
            FROM categories AS c
            LEFT JOIN interests AS i ON c.id = i.category_id
            LEFT JOIN profiles AS p ON i.profile_id = p.id WHERE p.country_code = ?
            GROUP BY c.id, c.name
            ORDER BY cumulative_relevance DESC
            '''
        data = read_query(query, (country_code,))

    else:
        query = '''
            SELECT c.id,
                   c.name,
                   COALESCE(SUM(i.relevance), 0) AS cumulative_relevance
            FROM categories AS c
            LEFT JOIN interests AS i ON c.id = i.category_id
            GROUP BY c.id, c.name
            ORDER BY cumulative_relevance DESC;
            '''
        data = read_query(query)

    if data:
        data = [CategoryRelevance.from_query_result(*row) for row in data]
    return data


# query = '''
#     SELECT c.id,
#            c.name,
#            COALESCE(SUM(i.relevance), 0) AS cumulative_relevance
#     FROM categories AS c
#     LEFT JOIN interests AS i ON c.id = i.category_id
#     LEFT JOIN profiles AS p ON i.profile_id = p.id AND p.country_code = ?
#     GROUP BY c.id, c.name
#     ORDER BY cumulative_relevance DESC
#     '''

def _response_object(data):
    pass
