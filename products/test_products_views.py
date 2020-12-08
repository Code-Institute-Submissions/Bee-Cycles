from django.test import TestCase
from .models import Product


class TestProductViews(TestCase):
 
    def test_get_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html') 