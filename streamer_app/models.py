from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=50)
	url = models.URLField()
	published_date = models.DateTimeField(default=timezone.now)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title

class Comment(models.Model):
	comment_on = models.ForeignKey(Movie, on_delete=models.CASCADE, default = None)
	text = models.TextField()
	published_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
