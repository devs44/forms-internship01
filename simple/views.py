from django.shortcuts import redirect
from django.views.generic import UpdateView,CreateView,ListView,DetailView
from django.utils import timezone
from .models import *
from .forms import NewTopicForm

class BoardListView(ListView):
    model = Board
    template_name ='simple/home.html'
    context_object_name = 'index'

class BoardDetailView(DetailView):
    model = Board
    template_name = 'simple/detail.html'
    context_object_name = 'board'

class TopicCreateView(CreateView):
    model = Topic
    form_class = NewTopicForm
    template_name = 'simple/new_topic.html'
    success_url = 'simple:create'
