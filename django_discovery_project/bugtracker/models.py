
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Issue(models.Model):
	issue_users = models.ManyToManyField(User)
	issue_name = models.CharField(max_length=50)
	issue_type = models.CharField(max_length=50)
	issue_date = models.DateField()

	def __unicode__(self):
		return self.issue_name


class Comment(models.Model):
	issue = models.ForeignKey(Issue)
	comment_made = models.TextField(blank=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return unicode(self.user)
	

