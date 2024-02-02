def str_len(the_string, min_len, max_len, err_for_len):
    if not min_len <= len(the_string) <= max_len:
        raise ValueError(err_for_len)
    return the_string


def len_n_alnum(the_string: str, min_len, max_len, err_for_len, err_for_symbols):
    str_len(the_string, min_len, max_len, err_for_len)
    if not the_string.isalnum():
        raise ValueError(err_for_symbols)
    return the_string


def password(p, min_len, max_len, err_for_len, err_for_symbols):
    str_len(p, min_len, max_len, err_for_len)
    for ch in p:
        if not ch.isalnum() and ch not in ['@', '*', '-', '_']:
            raise ValueError(err_for_symbols)
    return p


def intval(p, minp, maxp, err):
    if not minp <= p <= maxp:
        raise ValueError(err)
    return p
