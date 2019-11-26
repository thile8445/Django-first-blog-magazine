from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(null=True)
	posttype = models.CharField(max_length=50)
	def __str__(self):
		return self.title

class Comment(models.Model):
	Post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	body = models.TextField()