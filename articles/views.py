from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/home.html'
    context_object_name = 'index'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'index'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = '__all__'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/article_edit.html'
    fields = ['title','text']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    context_object_name = 'index'
    success_url = reverse_lazy('home')
