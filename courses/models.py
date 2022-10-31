from email.policy import default
from enum import unique
from django.db import models
from accounts.models import User


class Section(models.Model):
    nameofsection = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.nameofsection


class Lesson(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=200, default="")
    # course = models.ManyToManyField(Course, on_delete=models.CASCADE, default="")

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
    #csection = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "courses"
