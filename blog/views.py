from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    posts = Post.objects.order_by('id').reverse()
    return render(request,'blog/view_posts.html',{'posts':posts})

def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_view.html', {'post': post})

def addpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_view', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_view', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
