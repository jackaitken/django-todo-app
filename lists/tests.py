from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import ToDoList, Item

class ToDoListTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testemail@test.com',
            password='testpassword'
        )
        self.list = ToDoList.objects.create(
            owner=self.user,
            name='Test List'
        )
    
    def test_list_string_representation(self):
        self.assertEqual(str(self.list), "testuser's \"Test List\" List")

    def test_list_name(self):
        self.assertEqual(f"{self.list.name}", "Test List")
    
    def test_list_owner(self):
        self.assertEqual(self.list.owner, self.user)

class ItemTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testemail@test.com',
            password='testpassword'
        )
        self.test_list = ToDoList.objects.create(
            owner=self.user,
            name='Test List'
        )
        self.item = Item.objects.create(
            title='test item',
            completed=False,
            to_do_list=self.test_list
        )

    def test_item_string_representation(self):
        self.assertEqual(str(self.item), "test item")

    def test_item_title(self):
        self.assertEqual(self.item.title, 'test item')

    def test_item_on_list(self):
        self.assertEqual(self.item.to_do_list, self.test_list)

class HomePageTests(TestCase):
    pass

class ToDoListsTests(TestCase):

    def test_list_view(self):
        response = self.client.get(reverse('todolists'))
        self.assertEqual(response.status_code, 200)
