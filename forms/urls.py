
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app10_1.urls')),
    path('customers', include('customers.urls')),
    path('pages', include('pages.urls')),
    path('crud', include('crud.urls')),
    path('geeks', include('geeks.urls')),
    path('simple/', include('simple.urls')),
    path('articles/', include('articles.urls')),
    path('todo/', include('todo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
