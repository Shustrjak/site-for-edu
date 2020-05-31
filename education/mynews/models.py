from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Article(models.Model):
    TIME_TO_READ = (
        (1, 'easy'),
        (2, 'medium-easy'),
        (3, 'medium'),
        (4, 'medium-hard'),
        (5, 'hard'),
    )

    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    time_to_read = models.IntegerField(choices=TIME_TO_READ)
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_last_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def short_text(self):
        if len(self.text) > 30:
            return f'{self.text[:30]}...'
        return self.text

