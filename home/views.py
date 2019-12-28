from django.shortcuts import render ,redirect,HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
from blog.models import  Post,Comment
# Create your views here.
def index(request):
	return render(request,"home/base.html")
def logout(request):
	auth_logout(request)
	# return HttpResponseRedirect('/')
	post = Post.objects.all().order_by("-date")
	postl=post[3:8]
	postf = post[0:1]
	subpost = post[1:3]
	return render(request,"blog/index.html",{"posts":post,"postf":postf,"subpost":subpost,"postl":postl})

def register(request):
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('blog:index')
    # Display a blink or invalid form
    context = {'form': form}
    return render(request, 'home/register.html', context)	
