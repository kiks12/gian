from django.db import models
from accounts.models import User


class Lesson(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=200, default="")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name='course_creator')
    key = models.CharField(max_length=100, default="", unique=True)
    lessons = models.ManyToManyField(Lesson)
    students = models.ManyToManyField(User, related_name='course_students')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "courses"
