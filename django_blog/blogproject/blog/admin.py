from django.contrib import admin

# Register your models here.

from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_time', 'modifield_time', 'category', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
