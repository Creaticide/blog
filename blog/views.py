
from django.utils import timezone
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

class PostDetailView(generic.ListView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')