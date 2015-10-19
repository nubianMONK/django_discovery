from django.db import models

# Create your models here.

class MainCategory(models.Model):

	title = models.CharField(max_length=50)
	summary = models.CharField(max_length=180)

	def __unicode__(self):
		return self.title


class Challenge(models.Model):

	title = models.CharField(max_length=50)
	category = models.ForeignKey(MainCategory)
	summary = models.CharField(max_length =180)
	
	def __unicode__(self):
		return self.title

class Issue(models.Model):
	
	name = models.CharField(max_length=50)
	challenge = models.ManyToManyField(Challenge, through='ChallengeIssue')
	
	def __unicode__(self):
		return self.name

class Solution(models.Model):

	title = models.CharField(max_length=50)
	summary = models.CharField(max_length=180)

	def __unicode__(self):
		return self.title


class ChallengeIssue(models.Model):
	challenge =  models.ForeignKey(Challenge)
	issue = models.ForeignKey(Issue)
	
	
