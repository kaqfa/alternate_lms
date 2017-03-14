from django.db import models
from member.models import Member
from course.models import Course


class Post(models.Model):
    STATUS_CHOICES = (('a', 'Aktif'), ('i', 'Tidak Aktif'))
    course = models.ForeignKey(Course)
    response_to = models.ForeignKey('self', null=True)
    creator = models.ForeignKey(Member)
    content = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()
    status = models.CharField(max_length=1, default='a', choices=STATUS_CHOICES)
