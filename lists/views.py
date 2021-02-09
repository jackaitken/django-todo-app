from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404
from .models import ToDoList, Item

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todo_lists.html'

    def get_queryset(self):
        current_user = ToDoList.objects.filter(owner=self.request.user.id)
        return current_user

class ToDoListCreateView(CreateView):
    model = ToDoList
    template_name = 'list_new.html'
    fields = ('name',)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)