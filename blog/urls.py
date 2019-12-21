from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	# path('<int:pk>',views.view,name='view'),
	path('<int:pk>',views.view,name='view'),
	path('blog/',views.index,name='index'),
]