from django.db.models import Count, F
from django.shortcuts import render

from blog.models import Blog, Comment


# Create your views here.


def blog_list(request):
    posts = Blog.objects.annotate(
        comment_count=Count('comment'),
        author_name=F("author__username")
    ).values('id', 'title', 'comment_count', 'author_name', 'content', 'post_date', 'image')
    context = {
        "posts": posts
    }
    return render(request, 'blog.html', context)
