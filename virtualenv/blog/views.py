from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) #add posts for the template to use,'posts' is the name

def post_detail(request, pk): #pk is pass-in parameter from urls.py
    post = get_object_or_404(Post, pk=pk) #get only one post, post.pk is used in template post_list.html
    return render(request, 'blog/post_detail.html', {'post':post}) #pass-in post for template to use
    
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #after submit the form, brought back to the same view with all data in request.POST
        if form.is_valid():
            post = form.save(commit=False) #commit=False means that we don't want to save Post model yet, we want to add author first
            post.author = request.user
            #post.published_date = timezone.now() #save post as draft
            post.save() #will preserve changes
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm() #first time comes in is a empty page
    return render(request, 'blog/post_edit.html', {'form': form}) #pass=-in form (PostForm) to post_edit.html
    
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
    
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html',{'posts':posts})
    
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=post.pk)
   
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')