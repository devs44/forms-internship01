from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todo/home.html'
    form_class = TodoForm
    context_object_name = 'index'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/add.html'
    fields = '__all__'

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/delete.html'
    context_object_name = 'index'
    success_url = reverse_lazy('home')

# class TodoDetailView(DetailView):
#     model = Todo
#     template_name = 'todo/home.html'
#     context_object_name = 'index'
#

# def index(request):
#     mytodo = Todo.objects.order_by('id')
#     form = TodoForm()
#     context = { 'mytodo': mytodo, 'form': form }
#     return render(request, 'todo/home.html', context)


@require_POST
def addNewTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()
    return redirect('index')


def deleteTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
