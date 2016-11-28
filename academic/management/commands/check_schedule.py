import logging

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from optparse import make_option


logger = logging.getLogger('default')
logger.propagate = False


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '--level', '-l',
            help='Level of logging'
        ),
    )
    help = ('Check if the user has to go to the university')

    def handle(self, *args, **options):
        # Setting logging
        level = options.get('level')
        if level:
            try:
                logger.setLevel(getattr(logging, level.upper()))
            except AttributeError:
                pass

        User.objects.first()
        # TODO: make the magic

        logger.info("Done!")
