from models.comment import Comment
from models.constants.user_role import UserRole


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

    def __init__(self, username, firstname, lastname, password, user_role, is_admin, vehicles):
