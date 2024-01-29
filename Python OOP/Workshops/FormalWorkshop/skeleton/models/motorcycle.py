class Motorcycle:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CATEGORY_LEN_MIN = 3
    CATEGORY_LEN_MAX = 10
    CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'

    WHEELS_COUNT = 2

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
