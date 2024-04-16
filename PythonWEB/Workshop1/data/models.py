from datetime import date
from pydantic import BaseModel, constr

DEV_LEVELS = {'junior': 1, 'mid': 2, 'senior': 3, }
LEVEL_DEVS = {1: 'junior', 2: 'mid', 3: 'senior'}
PROJECT_STATUS_NUMS = {"open": 1, "closed": 0}
PROJECT_NUMS_STATUS = {1: "open", 0: "closed"}

levels_constr = constr(pattern=r'^(junior|mid|senior)$')
project_status_constr = constr(pattern=r'^(open|closed)$')


class Developer(BaseModel):
    id: int | None
    name: str
    level_str: levels_constr

    @classmethod
    def from_query_result(cls, id, name, level_str):
        return cls(
            id=id,
            name=name,
            level_str=level_str
        )


class Project(BaseModel):
    id: int | None
    name: str
    status: project_status_constr
    team_limit: int

    @classmethod
    def from_query_result(cls, id, name, status, team_limit):
        return cls(
            id=id,
            name=name,
            status=status,
            team_limit=team_limit
        )
