from django.contrib import admin
from .models import Post,Comment
# Register your models here.
class CommentLine(admin.TabularInline):
	model = Comment
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','posttype','date','body']
	list_filter = ['date']
	search_fields = ['title']
	inlines = [CommentLine]

admin.site.register(Post , PostAdmin)
# admin.site.register(Post)
# admin.site.register(Comment)