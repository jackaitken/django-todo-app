from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    pass

# class List(models.Model):
#     owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)    

# class Item(models.Model):
#     title = models.CharField(max_length=50)
#     list = models.ForeignKey(List, on_delete=models.CASCADE)

