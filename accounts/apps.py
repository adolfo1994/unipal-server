from __future__ import unicode_literals

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from accounts.signals import new_follower_created
