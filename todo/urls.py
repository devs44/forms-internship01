
from django.urls import path
from django.shortcuts import redirect
from .import views
from .views import *
urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('add', TodoCreateView.as_view(), name='add'),
    # path('<int:pk>', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', TodoDeleteView.as_view(), name='delete'),
    # path('', views.index, name='index'),
    # path('add', views.addNewTodo, name='add'),
    # path('complete/<todo_id>', views.completeTodo, name='complete'),
    # path('delete', views.deleteTodo, name='delete'),
]
