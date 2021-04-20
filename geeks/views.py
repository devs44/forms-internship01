

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import GeeksModel

class MyView(View):
	def get(self, request):
		return HttpResponse('result')

class GeeksCreate(CreateView):
    model = GeeksModel
    fields = ['title', 'description']


class GeeksList(ListView):
    model = GeeksModel
