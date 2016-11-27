from django.contrib.auth.models import User
from rest_framework import serializers

from academic.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    user = serializers.IntegerField(required=False)

    class Meta:
        model = Todo
        fields = ('due_date', 'priority', 'description', 'subject', 'user')

    def validate(self, attrs):
        attrs['user'] = User.objects.last().id
