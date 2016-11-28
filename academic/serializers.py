from django.contrib.auth.models import User

from rest_framework import serializers

from academic.models import Todo, ScheduleBlock, Schedule, Subject


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('name', 'semester')


class TodoSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer()

    class Meta:
        model = Todo
        fields = ('due_date', 'priority', 'description', 'subject', 'user')

    def create(self, validated_data):
        subject_data = validated_data.pop('subject')
        name = subject_data.get('name')
        semester = subject_data.get('semester')
        subject, created = Subject.objects.get_or_create(
            name=name, semester=semester)
        validated_data['subject'] = subject
        return super(TodoSerializer, self).create(validated_data)


class ScheduleBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleBlock
        fields = ('get_day_display', 'start_time', 'end_time')


class ScheduleSerializer(serializers.ModelSerializer):

    blocks = ScheduleBlockSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ('subject_group', 'blocks')
