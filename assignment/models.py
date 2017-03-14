from django.db import models
from member.models import Member
from course.models import Content, Course


class Assignment(models.Model):
    creator = models.ForeignKey(Member, related_name="creator")
    content = models.ForeignKey(Content)
    max_point = models.PositiveIntegerField(default=100)
    pass_grade = models.PositiveIntegerField(null=True)
    student_work = models.ManyToManyField(Member, through='StudentWork')


class StudentWork(models.Model):
    student = models.ForeignKey(Member)
    assignment = models.ForeignKey(Assignment)
    total_point = models.FloatField(null=True, default=0)
    created_at = models.DateField()
    updated_at = models.DateField()
    status = models.CharField(max_length=1, default='a')


class QuestionBank(models.Model):
    creator = models.ForeignKey(Member)
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    type = models.CharField(max_length=1, default='t')
    choice1 = models.CharField(max_length=255, null=True)
    choice2 = models.CharField(max_length=255, null=True)
    choice3 = models.CharField(max_length=255, null=True)
    choice4 = models.CharField(max_length=255, null=True)
    choice5 = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=1, default='a')
    status = models.CharField(max_length=1, default='a')
    assignment_quest = models.ManyToManyField(
        Assignment, through="AssignmentQuestion")


class AssignmentQuestion(models.Model):
    assignment = models.ForeignKey(Assignment)
    question = models.ForeignKey(QuestionBank)
    max_point = models.PositiveIntegerField()


class StudentQuestionWork(models.Model):
    student_work = models.ForeignKey(StudentWork)
    assignment_quest = models.ForeignKey(AssignmentQuestion)
    answer = models.TextField(null=True)
    filename = models.FileField(null=True)
    point = models.FloatField(null=True)
    revision = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=1, default='a')
