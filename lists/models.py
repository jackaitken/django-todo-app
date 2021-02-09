from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('todolists')

class Item(models.Model):
    title = models.CharField(max_length=225)
    completed = models.BooleanField(default=False)
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
