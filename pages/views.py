from django.shortcuts import render
from django.views.generic import ListView
from pages.models import Publisher
# Create your views here.
class PublisherListView(ListView):
    model = Publisher
    template_name="pages/about.html"
