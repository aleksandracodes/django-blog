from django.shortcuts import render
from django.views import generic
from .models import Post


# Create the view code
class PostList(generic.ListView):
    model = Post
    # status 1 for publish or 0 for a draft
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6  # limit number of posts that can appear on the front page