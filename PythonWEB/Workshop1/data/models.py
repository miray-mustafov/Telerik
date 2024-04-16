from datetime import date
from pydantic import BaseModel, constr

DEV_LEVELS = {
    'junior': 1,
    'mid': 2,
    'senior': 3,
}

PROJECT_STATUS = {
    "open": 1,
    "closed": 0
}


class Developer(BaseModel):
    id: int | None
    name: str
    level_str: str

    @classmethod
    def from_query_result(cls, id, name, level_str):
        return cls(
            id=id,
            name=name,
            level_str=level_str
        )


class Project:
    id: int | None
    name: str
    status: str
    team_limit: int

    @classmethod
    def from_query_result(cls, id, status, team_limit):
        return cls(
            id=id,
            status=status,
            team_limit=team_limit
        )
