from django.db import models
import datetime



class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	pub_date = models.DateTimeField(default=datetime.datetime.now())


	def __str__(self):
		return self.title