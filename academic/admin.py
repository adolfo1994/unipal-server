from django.contrib import admin

from academic.models import (
    Semester,
    Subject,
    SubjectGroup,
    Schedule,
    ScheduleBlock,
    Todo,
)


admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(SubjectGroup)
admin.site.register(Schedule)
admin.site.register(ScheduleBlock)
admin.site.register(Todo)
