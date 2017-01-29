from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	Title = models.CharField(max_length=100)
	Summary = models.TextField()
	Url = models.CharField(max_length=150)
	# Content = models.TextField()
	Image= models.ImageField()

	def __unicode__(self):
		return unicode(self.questionid)
	
	def __str__(self):
		return self.questioni