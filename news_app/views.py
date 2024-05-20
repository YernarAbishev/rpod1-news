from django.shortcuts import render, get_object_or_404
from .models import Post

def home_page(request):
    return render(request, "./home.html")

def news_page(request):
    posts = Post.objects.all().order_by('-posted_date')
    context = {
        'posts': posts
    }
    return render(request, "./news.html", context)

def news_detail_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, "./news-detail.html", context)
