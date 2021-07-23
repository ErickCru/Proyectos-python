from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def list_posts(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', {'posts': posts)

# def detail_post(request, pk):
#     post = Post.objects.get(id=pk)
#     return render(request, 'post.html', {'post': post})

class ListPost(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'


class DetailPost(DetailView):
    model = Post
    template_name = 'post.html'
