from django.views.generic  import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import Person
from .forms import PersonForm

class PersonListView(ListView):
    model = Person
    template_name = 'app10_1/person/list.html'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'app10_1/person/form.html'
    success_url = 'app10_1:create'

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'app10_1/person/form.html'
    success_url = reverse_lazy('app10_1:persons')

class PersonDetailView(DetailView):
    model = Person
    template_name = 'app10_1/person/detail.html'

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('persons')
