from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',views.index,name='index'),
	path( 'login/',auth_views.LoginView.as_view(template_name="home/login.html"), name="login"),
	# path('logout/',view_auth.LogoutView.as_view(template_name = 'blog/base.html'),name="logout"),
	path('logout/',views.logout,name='logout'),
	path('register/',views.register,name='register'),
]