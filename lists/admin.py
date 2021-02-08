from django.contrib import admin
from .models import CustomUser, ToDoList, Item
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ToDoList)
admin.site.register(Item)