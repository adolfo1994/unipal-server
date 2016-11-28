from django.contrib.auth.models import User

from rest_framework import serializers

from academic.models import Todo, ScheduleBlock, Schedule


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('due_date', 'priority', 'description', 'subject', 'user')


class ScheduleBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleBlock
        fields = ('get_day_display', 'start_time', 'end_time')


class ScheduleSerializer(serializers.ModelSerializer):

    blocks = ScheduleBlockSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ('subject_group', 'blocks')
