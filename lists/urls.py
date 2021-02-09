from django.urls import path
from .views import SignUpView, ToDoListView, ToDoListCreateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/todolists', ToDoListView.as_view(), name='todolists'),
    path('new/', ToDoListCreateView.as_view(), name='list_new')
]