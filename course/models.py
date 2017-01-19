from django.db import models
from member.models import Member

class Course(models.Model):
	creator = models.ForeignKey(Member)
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=255)
	description = models.TextField(null=True)
	credit = models.PositiveIntegerField()
	status = models.CharField(max_length=1, default='a')

class Section(models.Model):
	course = models.ForeignKey(Course)
	title = models.CharField(max_length=255)
	description = models.TextField(null=True)
	status = models.CharField(max_length=1, default='a')

class ContentType(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True)

class Content(models.Model):
	section = models.ForeignKey(Section)
	title = models.CharField(max_length=255)
	description = models.TextField(null=True)
	available_from = models.DateField()
	available_to = models.DateField(null=True)
	type = models.ForeignKey(ContentType)
	status = models.CharField(max_length=1, default='a')
