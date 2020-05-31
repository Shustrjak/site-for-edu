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
    TTR_EASY = 1
    TTR_M_EASY = 2
    TTR_M = 3
    TTR_M_H = 4
    TTR_H = 5
    TIME_TO_READ = (
        (TTR_EASY, 'easy'),
        (TTR_M_EASY, 'medium-easy'),
        (TTR_M, 'medium'),
        (TTR_M_H, 'medium-hard'),
        (TTR_H, 'hard'),
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
