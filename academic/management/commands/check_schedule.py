import logging

from datetime import datetime, date, timedelta

from django.core.management.base import BaseCommand

from academic.models import ScheduleBlock


logger = logging.getLogger('default')
logger.propagate = False


class Command(BaseCommand):
    help = ('Check if the user has to go to the university')

    def add_arguments(self, parser):
        parser.add_argument(
            '--level',
            default=False,
            help='Level of logging'
        )

    def send_notification(self, block):
        # FIXME: If no notifications are sent is because this function is wrong
        if (
            (datetime.now().weekday() == block.day) and
            (
                datetime.combine(date.today(), block.start_time) -
                datetime.now()
            ).min < timedelta(minutes=45)
        ):
            return True
        return False

    def handle(self, *args, **options):
        # Setting logging
        level = options.get('level')
        if level:
            try:
                logger.setLevel(getattr(logging, level.upper()))
            except AttributeError:
                pass

        for block in ScheduleBlock.objects.all():
            if self.send_notification(block):
                for user in block.schedule.subject_group.users.all():
                    for device in user.gcmdevice_set.all():
                        device.send_message(
                            "Nada mas no vas a faltar a %s en %s" % (
                                block.schedule.subject_group.subject.name,
                                block.location,
                            )
                        )
        logger.info("Done!")
