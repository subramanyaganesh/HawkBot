from django.core.management.base import BaseCommand
from .core import Core

class Command(BaseCommand):
    help = 'cron job'

    def handle(self, *args, **options):
        Core.core()
        self.stdout.write(self.style.SUCCESS('Cron job executed successfully.'))
        
