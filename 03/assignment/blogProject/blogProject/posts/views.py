from django.shortcuts import render, redirect

from posts.serializers import PostSerializer
from .models import Post,Comment
from django.http import Http404
from .forms import PostForm,CommentForm
from rest_framework import generics
# Create your views here.
def post_list(request):
  posts = Post.objects.all()
  context = {"posts":posts}
  return render(request, 'posts/post_list.html',context)

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  comment = Comment.objects.filter(post=post)
  
  if request.method == 'POST':
    comment_form = CommentForm(request.POST)
    
    new_comment = comment_form.save()
    new_comment.author = request.user
    new_comment.post = post
    new_comment.save()
    return redirect('post-detail',post_id = post.id)
  else:
    comment_form = CommentForm()

  context = {"post":post, "comment":comment,'form':comment_form}
  return render(request,'posts/post_detail.html',context)

def post_create(request):
  if not request.user.is_authenticated:
      raise Http404
  if request.method == 'POST':
    post_form = PostForm(request.POST)
    new_post = post_form.save()
    new_post.author = request.user
    new_post.save()
    return redirect('post-detail',post_id = new_post.id)
  else:
    post_form = PostForm()
    return render(request, 'posts/post_form.html',{'form':post_form})
  
def post_update(request, post_id):
  
  post = Post.objects.get(id = post_id)
  if post.author != request.user:
    raise Http404
  if request.method =='POST':
    post_form = PostForm(request.POST, instance=post)
    post_form.save()
    return redirect('post-detail',post_id=post.id)
  else:
    post_form = PostForm(instance=post)
  return render(request, 'posts/post_form.html',{'form':post_form})

def post_delete(request,post_id):
  post = Post.objects.get(id=post_id)
  if request.method == 'POST':
    post.delete()
    return redirect('post-list')
  else:
    return render(request, 'posts/post_confirm_delete.html',{'post':post})
  
def index(request):
  return redirect('post-list')

class PostListCreateAPI(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer