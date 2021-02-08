from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    pass

class ToDoList(models.Model):
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
        )    
    name = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.owner}\'s \"{self.name}\" List"

class Item(models.Model):
    on_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    item_to_add = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return f"\"{self.item_to_add}\" on {self.on_list}"