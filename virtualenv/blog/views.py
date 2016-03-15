from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) #add posts for the template to use,'posts' is the name

def post_detail(request, pk): #pk is pass-in parameter from urls.py
    post = get_object_or_404(Post, pk=pk) #get only one post
    return render(request, 'blog/post_detail.html', {'post':post}) #pass-in post for template to use