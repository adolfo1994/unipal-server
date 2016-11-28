from django.db.models.signals import post_save
from django.dispatch import receiver

from push_notifications.models import GCMDevice
from friendship.models import Follow


# FUTURE: move to devices app
@receiver(post_save, sender=Follow, dispatch_uid='follower_created')
def follower_created(sender, instance=None, **kwargs):
    """
    Notifies the user that has a new follower

    :param sender: Model that sends the signal
    :param instance: Instance of the model
    """

    # FUTURE: link GCMDevice to a User
    for device in GCMDevice.objects.all():
        device.send_message("Tienes un nuevo seguidor")
