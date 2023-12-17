from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# from taggit.managers import TaggableManager

# Create your models here.

	
class Note(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
	title = models.CharField(max_length=120)
	
	date = models.DateTimeField(default=timezone.now)
	content  = models.TextField()
	tags = models.ManyToManyField('Tag')

	def __str__(self):
		return f'{self.title}'

	def get_absolute_url(self):
		return reverse('notes-detail', kwargs={"pk":self.pk})


class Tag(models.Model):
	name = models.CharField(max_length=100)
	slug =models.SlugField(max_length=20, unique=True)

	def __str__(self):
		return self.name