import factory
from django.core.management import BaseCommand
from factory.django import DjangoModelFactory
from ...models import Author, Article
from faker import Faker

fake = Faker()


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('word')
    text = factory.Faker('text')
    author = factory.SubFactory(AuthorFactory)
    time_to_read = factory.Iterator(['1', '2', '3', '4', '5'])


def create_all():
    # author = AuthorFactory()
    # print(author)
    # authors = AuthorFactory.build_batch(5)
    # print(authors)
    # authors = AuthorFactory.create_batch(5)
    # print(authors)
    article = ArticleFactory()
    print(article, article.author)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_all()
        self.stdout.write(self.style.SUCCESS('Done'))
