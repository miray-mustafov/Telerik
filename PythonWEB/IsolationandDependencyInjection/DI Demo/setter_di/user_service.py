from database import DBConnection

class UserService:
    def __init__(self) -> None:
        self.database = None
    
    def set_database(self, database: DBConnection):
        self.database = database

    def get_user_by_id(self, id: int):
        user = self.database.read_query()
        #some business logic here
        return user
    