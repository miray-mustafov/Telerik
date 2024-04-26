import unittest
from unittest.mock import Mock
from data.models import Category, Product
from routers import categories as categories_router
from common.responses import NotFound

mock_category_service = Mock(spec='services.category_service')
mock_product_service = Mock(spec='services.product_service')
categories_router.category_service = mock_category_service
categories_router.product_service = mock_product_service

def fake_category(id=1, name='Test_category'):
    mock_category = Mock(spec=Category)
    mock_category.id = id
    mock_category.name = name
    return mock_category

def fake_product(id=1, name='Test_product', description='Test_description', price=1.00, category_id=1):
    mock_product = Mock(spec=Product)
    mock_product.id = id
    mock_product.name = name
    mock_product.description=description
    mock_product.category_id=category_id
    return mock_product


class CategoryRouter_Should(unittest.TestCase):

    def setUp(self) -> None:
        mock_category_service.reset_mock()
        mock_product_service.reset_mock()
        

    def test_getCategoryById_returns_NotFound_when_noCategory(self):
        mock_category_service.get_by_id = lambda id: None
        result = type(categories_router.get_category_by_id(1))
        expected = NotFound
        self.assertEqual(expected, result)

    def test_getCategoryById_returns_CategoryResponse_when_categoryIsPresent(self):
        category = fake_category()
        product = fake_product()
        mock_category_service.get_by_id = lambda id: category
        mock_product_service.get_by_category = lambda cat_id: [product]

        result = categories_router.get_category_by_id(category.id)
        expected = categories_router.CategoryResponseModel(category=category, products=[product])
        self.assertEqual(expected, result)
        self.assertEqual(expected.category, result.category)
        self.assertEqual(expected.products, result.products)

    def test_getCategories_returns_emptyList_when_noCategories(self):
        mock_category_service.all = lambda: []
        self.assertEqual([], categories_router.get_categories())

    def test_getCategories_returns_listOfResponseModels_when_categoriesArePresent(self):
        category0 = fake_category(id=0)
        category1 = fake_category(id=1)
        product1 = fake_product(category_id=1)
        product_pool = [[], [product1]]
        mock_category_service.all = lambda: [category0, category1]
        mock_product_service.get_by_category = lambda cat_id: product_pool[cat_id]
        result = categories_router.get_categories()
        expected = [
            categories_router.CategoryResponseModel(category=category0, products=[]),
            categories_router.CategoryResponseModel(category=category1, products=[product1])
        ]
        self.assertEqual(expected, result)

    def test_createCategory_returns_ResponseModelWithEmptyProductList_when_categoryIsValid(self):
        category = fake_category()
        mock_category_service.create = lambda cat: category
        result = categories_router.create_category(category)
        expected = categories_router.CategoryResponseModel(
            category=category,
            products=[]
        )
        self.assertEqual(expected, result)


        