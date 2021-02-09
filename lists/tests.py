from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import ToDoList

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
    
    def test_string_representation(self):
        to_do_list = ToDoList(
            owner=self.user,
            name='Test List'
        )
        self.assertEqual(str(to_do_list), "testuser's \"Test List\" List")

    def test_list_name(self):
        self.assertEqual(f"{self.list.name}", "Test List")
    
    def test_list_owner(self):
        self.assertEqual(f"{self.list.owner}", f"{self.user}")

    def test_list_view(self):
        response = self.client.get(reverse('todolists'))
        self.assertEqual(response.status_code, 200)