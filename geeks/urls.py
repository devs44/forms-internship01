# urls.py
from django.urls import path
from geeks.views import MyView
from .views import *
urlpatterns = [
	path('', GeeksCreate.as_view()),
	path('about/', MyView.as_view()),
	path('', GeeksList.as_view()),
]
