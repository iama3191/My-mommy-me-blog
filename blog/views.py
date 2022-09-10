from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListViews):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginated_by = 6
