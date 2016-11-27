from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Semester(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField()


class Subject(models.Model):
    name = models.CharField(max_length=250)
    semester = models.ForeignKey(Semester)


class SubjectGroup(models.Model):
    subject = models.ForeignKey(Subject)
    users = models.ManyToManyField(User)


class Schedule(models.Model):
    subject_group = models.ForeignKey(SubjectGroup)


class ScheduleBlock(models.Model):
    DAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    day = models.PositiveSmallIntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Todo(models.Model):
    PRIORITY_CHOICES = (
        (0, 'Low'),
        (1, 'Medium'),
        (2, 'High'),
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES)
    description = models.CharField(max_length=250)
    subject = models.ForeignKey(Subject)
    user = models.ForeignKey(User)
