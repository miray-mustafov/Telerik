from pydantic import BaseModel, constr, conint


class DevLevelMaps:
    INT_TO_STR = {1: 'junior', 2: 'mid', 3: 'senior'}
    STR_TO_INT = {'junior': 1, 'mid': 2, 'senior': 3}


class Project(BaseModel):
    id: int | None
    name: constr(min_length=1)
    status: constr(regex='^open|closed$')
    limit: conint(ge=1)
    devs: list = []

    @classmethod
    def from_query_result(cls, id, name, is_open, team_limit, devs=None):
        return cls(
            id=id,
            name=name,
            status='open' if is_open else 'closed',
            limit=team_limit,
            devs=devs or [])


class Dev(BaseModel):
    id: int | None
    name: constr(min_length=1)
    level: constr(regex='^junior|mid|senior$')
    projects: list = []

    @classmethod
    def from_query_result(cls, id, name, level, projects=None):
        return cls(
            id=id,
            name=name,
            level=DevLevelMaps.INT_TO_STR[level],
            projects=projects or [])
