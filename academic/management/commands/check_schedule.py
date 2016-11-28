import logging

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
        # TODO: check hour range
        return True

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
