from django.db import models
from django.contrib.auth.models import User

class Member(User):
	MEMBER_TYPE = (
			('s', 'mahasiswa'), 
			('l', 'dosen')
		)
	address = models.CharField(max_length=255, null=True)
	phone = models.CharField(max_length=20, null=True)
	type = models.CharField(max_length=1, default='s', choices=MEMBER_TYPE)
	status = models.CharField(max_length=1, default='a')

class UserLog(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	activity  = models.CharField(max_length=255)
