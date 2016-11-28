from __future__ import unicode_literals

from django.apps import AppConfig


class AcademicConfig(AppConfig):
    name = 'academic'

    def ready(self):
        from academic.signals import todo_created
