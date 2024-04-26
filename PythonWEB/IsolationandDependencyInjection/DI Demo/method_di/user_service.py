from database import DBConnection

class UserService:
    def __init__(self) -> None:
        pass

    def get_user_by_id(self, id: int, database: DBConnection):
        user = database.read_query()
        #some business logic here
        return user
    