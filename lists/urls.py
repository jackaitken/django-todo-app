from django.urls import path
from .views import SignUpView, ToDoListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('todolists/', ToDoListView.as_view(), name='todolists'),
]