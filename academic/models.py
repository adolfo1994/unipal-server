from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Semester(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.slug


class Subject(models.Model):
    name = models.CharField(max_length=250)
    semester = models.ForeignKey(Semester)

    def __unicode__(self):
        return "{name} - {semester}".format(
            name=self.name, semester=self.semester.slug
        )


class SubjectGroup(models.Model):
    subject = models.ForeignKey(Subject)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return "{name} - {slug}".format(
            name=self.subject.name,
            slug=self.subject.semester.slug
        )


class Schedule(models.Model):
    subject_group = models.ForeignKey(SubjectGroup)

    @property
    def blocks(self):
        return self.scheduleblock_set.all()


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
    schedule = models.ForeignKey(Schedule)
    location = models.CharField(max_length=250)

    def __unicode__(self):
        return "{day} - {start} - {end}".format(
            day=self.day, start=self.start_time, end=self.end_time
        )


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
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return "{subject} - {user}".format(
            subject=self.subject.name,
            user=self.user.username
        )