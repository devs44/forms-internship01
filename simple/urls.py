from django.conf.urls import url
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('details/<int:pk>/',BoardDetailView.as_view(), name='detail'),
    path('details/<int:pk>/new/', TopicCreateView.as_view(), name='create'),
]
