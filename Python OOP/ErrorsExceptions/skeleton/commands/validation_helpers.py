from errors.invalid_params import InvalidParams


def try_parse_float(float_string: str, msg: str):
    try:
        return float(float_string)
    except:
        raise ValueError(msg)


def validate_params_count(params, count, cmd_name):
    if len(params) != count:
        raise InvalidParams(cmd_name, count)
