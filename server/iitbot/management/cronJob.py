from django.core.management.base import BaseCommand
from django.core.cache import cache
from .core import Core
from .models import DynamicModel

class Command(BaseCommand):
    help = 'cron job'

    def handle(self, *args, **options):
        dynamic_instance = DynamicModel(data={'hawk_bot': Core.core()})
        dynamic_instance.save()
        # cache.set('hawk_bot', Core.core(), timeout=None) 
