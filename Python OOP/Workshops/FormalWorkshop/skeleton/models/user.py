from models.comment import Comment
from models.constants.user_role import UserRole
from core import validate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vehicle import Vehicle


class User:
    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    def __init__(self, username, firstname, lastname, password, user_role=UserRole.NORMAL):
        self._username = validate.len_n_alnum(username, User.USERNAME_LEN_MIN, User.USERNAME_LEN_MAX,
                                              User.USERNAME_LEN_ERR,
                                              User.USERNAME_INVALID_SYMBOLS)
        self._firstname = validate.str_len(firstname, User.FIRSTNAME_LEN_MIN, User.FIRSTNAME_LEN_MAX,
                                           User.FIRSTNAME_LEN_ERR)
        self._lastname = validate.str_len(lastname, User.LASTNAME_LEN_MIN, User.LASTNAME_LEN_MAX,
                                          User.LASTNAME_LEN_ERR)
        self._password = validate.password(password, User.PASSWORD_LEN_MIN, User.PASSWORD_LEN_MAX,
                                           User.PASSWORD_LEN_ERR, User.PASSWORD_INVALID_SYMBOLS)
        self._user_role: UserRole = user_role  # UserRole.from_string(user_role)
        self._is_admin = True if self._user_role == UserRole.ADMIN else False
        self._vehicles = []
        self._comments: list[Comment] = []

    @property
    def username(self):
        return self._username

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def password(self):
        return self._password

    @property
    def user_role(self):
        return self._user_role

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def vehicles(self):
        return tuple(self._vehicles)

    @property
    def comments(self):
        return tuple(self._comments)

    def add_vehicle(self, vehicle: 'Vehicle'):  # ?
        if self.is_admin:
            raise ValueError(User.ADMIN_CANNOT_ADD_VEHICLES_ERR)
        elif self.user_role == UserRole.NORMAL and len(self.vehicles) == User.NORMAL_ROLE_VEHICLE_LIMIT:
            raise ValueError(User.NORMAL_USER_LIMIT_REACHED_ERR)
        self._vehicles.append(vehicle)

    def get_vehicle(self, index: int):
        if index >= len(self.vehicles):
            raise ValueError('The vehicle does not exist!')
        return self._vehicles[index]

    def remove_vehicle(self, vehicle: 'Vehicle'):
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)

    # todo
    def add_comment(self, content: str, vehicle: 'Vehicle'):
        cmnt = Comment(content, self.username)
        vehicle.add_comment(cmnt)

    # todo
    def remove_comment(self, comment: 'Comment', vehicle: 'Vehicle'):
        if self.username == comment.author:
            vehicle.remove_comment(comment)
            return
        raise ValueError('You are not the author of the comment you are trying to remove!')

    def print_vehicles(self):
        res = [f'--USER {self.username}--']
        if not self._vehicles:
            vehicles_msg = ['--NO VEHICLES--']
        else:
            vehicles_msg = []
            for i, vhcl in enumerate(self._vehicles):
                vehicles_msg.append(f'{i + 1}. {vhcl}')

        res.extend(vehicles_msg)
        return '\n'.join(res)

    def __str__(self):
        return f'Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self.user_role}'
