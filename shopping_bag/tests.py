from django.test import TestCase, Client
from django.shortcuts import reverse, HttpRequest
from products.models import Product
from .models import Bag, OrderLineItem, BagManager

from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.conf import settings
from importlib import import_module
# Create your tests here.


class TestBagViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword'
        )
        self.shopping_bag_url = reverse('shopping_bag')

    def test_shopping_bag_view(self):
        response = self.client.get(self.shopping_bag_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_bag/shopping_bag.html')

    def test_add_to_shopping_bag(self):
        product = Product.objects.create(
            name='testing edit',
            gender='man',
            description='test desc',
            price=20.2,
            quantity=1
        )
        self.client.post(
            '/shopping_bag/add/', {' product_id': product.id, 'quantity': 1}
        )

    def test_alter_shoping_bag(self):
        product = Product.objects.create(
            name='testing edit',
            gender='man',
            description='test desc',
            price=20.2,
            quantity=1
        )
        self.client.post(
            '/shopping_bag/remove_from_bag/',
            {' product_id': product.id, 'quantity': 1}
        )

    def test_remove_from_bag(self):
        product = Product.objects.create(
            name='testing edit',
            gender='man',
            description='test desc',
            price=20.2,
            quantity=1
        )
        self.client.post(
            '/shopping_bag/alter_shoping_bag/', {' product_id': product.id}
        )


class TestShoppingBagModels(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword'
        )
        self.product = Product.objects.create(
            name='testing model',
            gender='man',
            description='test desc',
            price=20.2,
            quantity=1
        )

    def test_orderlineitem_model(self):
        orderlinitem = OrderLineItem.objects.create(
                product=self.product,
                product_size='xx',
                quantity=1,
        )
        self.assertEqual(orderlinitem.product, self.product)

    def test_bag_model(self):
        bag = Bag.objects.create(
            user=self.user,
            subtotal=2.44,
            total=22.3
        )
        self.assertEqual(bag.id, bag.id)

    # def test_bag_manager(self):
    #     request = HttpRequest()
    #     engine = import_module(settings.SESSION_ENGINE)
    #     session_key = None
    #     request.session = engine.SessionStore(session_key)
    #     bag = Bag.objects.create(
    #         user = self.user,
    #         subtotal = 2.44,
    #         total = 22.3
    #     )
    #     bag_func = Bag.objects.new_or_get(request)
    #     self.assertTrue(bag_func)