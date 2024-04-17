from datetime import date
from pydantic import BaseModel, constr, PositiveInt, Field

# to translate data to the database
DEV_LEVELS = {'junior': 1, 'mid': 2, 'senior': 3, }
LEVEL_DEVS = {1: 'junior', 2: 'mid', 3: 'senior'}
PROJECT_STATUS_NUMS = {"open": 1, "closed": 0}
PROJECT_NUMS_STATUS = {1: "open", 0: "closed"}


class Developer(BaseModel):
    id: int | None = None
    name: str = Field(min_length=1)
    level_str: constr(pattern=r'^(junior|mid|senior)$')

    @classmethod
    def from_query_result(cls, id, name, level_str):
        return cls(
            id=id,
            name=name,
            level_str=level_str
        )


class ProjectStatusUpdate(BaseModel):
    status: constr(pattern=r'^(open|closed)$')


class Project(BaseModel):
    id: int | None = None
    name: str = Field(min_length=1)
    status: constr(pattern=r'^(open|closed)$')
    team_limit: PositiveInt

    @classmethod
    def from_query_result(cls, id, name, status, team_limit):
        return cls(
            id=id,
            name=name,
            status=status,
            team_limit=team_limit
        )

# tst_dev = Developer(name='123', level_str='junio') # ValidationError
# print(tst_dev)
