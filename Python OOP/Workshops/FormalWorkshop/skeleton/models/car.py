class Car:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CAR_SEATS_MIN = 1
    CAR_SEATS_MAX = 10
    CAR_SEATS_ERR = f'Seats must be between {CAR_SEATS_MIN} and {CAR_SEATS_MAX}!'

    WHEELS_COUNT = 4

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file