from django.db.models import Count, F
from django.shortcuts import render

from blog.models import Blog, Comment

from blog.forms import CommentForm


# Create your views here.


def blog_list(request):
    posts = Blog.objects.annotate(
        comment_count=Count('comment'),
        author_name=F("author__username")
    ).values('id', 'title', 'comment_count', 'author_name', 'content', 'post_date', 'image')
    print(posts)
    context = {
        "posts": posts
    }
    return render(request, 'blog.html', context)


def blog_detail(request, pk):

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = Blog.objects.get(id=pk)
            comment.author = request.user
            comment.save()
    posts = Blog.objects.all()
    post = Blog.objects.annotate(
        comment_count=Count('comment'),
        author_name=F("author__username")
    ).filter(id=pk).values('id', 'title', 'comment_count', 'author_name', 'content', 'post_date', 'image')

    comments = Comment.objects.filter(post_id=pk).select_related('author')
    form = CommentForm()
    context = {
        'posts': posts,
        'post': post[0],
        'comments': comments,
        'form': form
    }
    print(posts[0])
    return render(request, 'single-post.html', context)
