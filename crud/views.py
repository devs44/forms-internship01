
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Blogs

class IndexView(ListView):
    model = Blogs
    queryset = Blogs.objects.filter(status='published').all(). \
        order_by('-published_at')
    template_name = 'crud/list_view.html'
    context_object_name = 'index_post_list'

class DetailedView(DetailView):
    model = Blogs
    template_name = 'crud/detail_view.html'
    context_object_name = 'post'
