from django.core.management import BaseCommand
from mixer.backend.django import mixer
from ...models import Author
from faker import Faker

fake = Faker()


def create_all():
    author = mixer.blend(Author)
    print(author)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_all()
