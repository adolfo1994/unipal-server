from rest_framework import viewsets

from academic.models import Todo, Schedule
from academic.serializers import TodoSerializer, ScheduleSerializer


class TodoViewSet(viewsets.ModelViewSet):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class ScheduleViewSet(viewsets.GenericViewSet,
                      viewsets.mixins.ListModelMixin,
                      viewsets.mixins.RetrieveModelMixin):

    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
