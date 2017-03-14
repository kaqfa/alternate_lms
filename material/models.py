from django.db import models
from member.models import Member
from course.models import Content


class Material(models.Model):
    STATUS_CHOICES = (('a', 'Aktif'), ('i', 'Tidak Aktif'))

    creator = models.ForeignKey(Member)
    content = models.OneToOneField(Content)
    filename = models.FileField(upload_to='uploads/material', null=True)
    url = models.CharField(max_length=255, null=True)
    text = models.TextField(null=True)
    type = models.CharField(max_length=1)
    status = models.CharField(max_length=1, default='a', choices=STATUS_CHOICES)
