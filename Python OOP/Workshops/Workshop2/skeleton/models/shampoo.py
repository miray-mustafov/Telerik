from models.product import Product


def _validate_usage_type(value):
    if value not in ['Every_Day', 'Medical']:
        raise ValueError('Usage type can be one of "Every_Day" or "Medical"')


def _validate_milliliters(value):
    if value < 0:
        raise ValueError('Invalid mill cannot be negative.')


def _swap_if_needed(milliliters, usage_type):
    if isinstance(usage_type, int):
        milliliters, usage_type = usage_type, milliliters

    return milliliters, usage_type


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, milliliters, usage_type):
        super().__init__(name, brand, price, gender)
        milliliters, usage_type = _swap_if_needed(milliliters, usage_type)
        _validate_milliliters(milliliters)
        _validate_usage_type(usage_type)
        self._usage_type = usage_type
        self._milliliters = milliliters

    @property
    def usage_type(self):
        return self._usage_type

    @property
    def milliliters(self):
        return self._milliliters

    def to_string(self):
        res = super().to_string()
        res += f'\n #Milliliters: {self.milliliters}' \
               f'\n #Usage: {self.usage_type}'
        return res
