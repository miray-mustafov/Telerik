import unittest
from models.product import Product
from models.gender import Gender

VALID_NAME = 'testname'
VALID_BRAND = 'testbrand'
VALID_PRICE = 2
VALID_GENDER = Gender.MEN


class Product_Should(unittest.TestCase):
    def test_init_set_props(self):
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        self.assertEqual(VALID_NAME, product.name)
        self.assertEqual(VALID_BRAND, product.brand)
        self.assertEqual(VALID_PRICE, product.price)
        self.assertEqual(VALID_GENDER, product.gender)

    def test_init_raiseError_nameToo_short(self):
        with self.assertRaises(ValueError):
            Product('a', VALID_BRAND, VALID_PRICE, VALID_GENDER)

    def test_init_raiseError_gender_invalid(self):
        with self.assertRaises(ValueError):
            Product(VALID_NAME, VALID_BRAND, VALID_PRICE, 'Mean')
