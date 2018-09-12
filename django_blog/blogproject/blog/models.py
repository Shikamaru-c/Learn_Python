from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import markdown
from django.utils.html import strip_tags
# Create your models here.

class Category(models.Model): # 分类
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=70)
	body = models.TextField()


	created_time = models.DateTimeField(auto_now_add=True)
	modifield_time = models.DateTimeField(auto_now_add=True)
	excerpt = models.CharField(max_length=200, blank=True) # 摘要

	def save(self, *args, **kwargs):
		if not self.excerpt:
			md = markdown.Markdown(extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
				])
			self.excerpt = strip_tags(md.convert(self.body))[:54]

		super(Post, self).save(*args, **kwargs)

	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)

	author = models.ForeignKey(User)

	views = models.PositiveIntegerField(default=0) # 阅读量

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk': self.pk})

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views']) # 增加阅读量

	class Meta:
		ordering = ['-created_time']
