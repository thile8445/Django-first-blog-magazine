from django.shortcuts import render ,get_object_or_404
from .models import Post,Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
	post = Post.objects.all().order_by("-date")
	postf = post[0:1]
	subpost = post[1:3]
	return render(request,"blog/index.html",{"posts":post,"postf":postf,"subpost":subpost})

def view(request,pk):
	post = Post.objects.filter(pk = pk)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST,author = request.user ,post = post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	return render(request,"blog/view.html",{"post":post,"form":form })

