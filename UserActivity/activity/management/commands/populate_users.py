from django.core.management.base import BaseCommand
import factory
from activity import factories

class Command(BaseCommand):
    help = 'Creates users.'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        with factory.Faker.override_default_locale('en_US'):
            for i in range(total):
                factories.UserFactory.create()
