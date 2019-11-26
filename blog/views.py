from django.shortcuts import render ,get_object_or_404
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
# Create your views here.
def index(request):
	post = Post.objects.all().order_by("-date")
	postf = post[0:1]
	subpost = post[1:3]
	return render(request,"blog/index.html",{"posts":post,"postf":postf,"subpost":subpost})

def view(request,pk):
	# post = get_object_or_404 (Post , pk = pk)
	# post = Post.objects.all()
	posts = Post.objects.filter(pk = pk)
	# post = get_object_or_404( Post , pk=pk)
	# post = post(pk = pk)
	return render(request,"blog/view.html",{"posts":posts})

