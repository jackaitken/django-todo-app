from django.urls import path
from .views import (
    SignUpView,
    ToDoListView,
    ToDoListCreateView,
    ItemCreateView,  
    ToDoListDeleteView
) 

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/todolists/', ToDoListView.as_view(), name='todolists'),
    path('list_new/', ToDoListCreateView.as_view(), name='list_new'),
    path('<int:pk>/item_new/', ItemCreateView.as_view(), name='item_new'),
    path('<int:pk>/delete/', ToDoListDeleteView.as_view(), name='list_delete')
]