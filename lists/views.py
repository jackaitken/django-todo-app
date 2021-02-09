from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import CreateView, ListView
from .models import ToDoList

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todo_lists.html'

class ToDoListCreateView(CreateView):
    model = ToDoList
    template_name = 'list_new.html'
    fields = ('name',)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)