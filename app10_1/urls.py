from django.urls import path
from . import views
app_name = 'app10_1'

urlpatterns = [
    path('', views.PersonListView.as_view(), name='persons'),
    path('person/', views.PersonCreateView.as_view(), name='create'),
    path('person/details/<int:pk>', views.PersonDetailView.as_view(), name='details'),
    path('person/update/<int:pk>', views.PersonUpdateView.as_view(),name='update'),
    path('person/delete/<int:pk>', views.PersonDeleteView.as_view(),name='delete'),
]
