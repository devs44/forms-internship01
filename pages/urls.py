

from django.urls import path
from pages.views import PublisherListView

urlpatterns = [
    path('publishers/', PublisherListView.as_view()),

]
