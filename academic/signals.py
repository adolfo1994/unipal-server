from django.db.models.signals import post_save
from django.dispatch import receiver

from push_notifications.models import GCMDevice

from academic.models import Todo


@receiver(post_save, sender=Todo, dispatch_uid='todo_created')
def todo_created(sender, instance=None, **kwargs):
    """
    Notifies the user that has a new todo

    :param sender: Model that sends the signal
    :param instance: Instance of the model
    """

    for device in GCMDevice.objects.all():
        device.send_message(
            "Han agregado una nueva tarea!", extra={'title': 'Nueva Tarea!'})
