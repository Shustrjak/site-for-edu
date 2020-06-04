from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Lesson(models.Model):
    DS_1 = 1
    DS_2 = 2
    DS_3 = 3
    DS_4 = 4
    DS_5 = 5
    DIFFICULT_STAR = (
        (DS_1, '1 star'),
        (DS_2, '2 stars'),
        (DS_3, '3 stars'),
        (DS_4, '4 stars'),
        (DS_5, '5 stars'),
    )

    title = models.CharField(max_length=50)
    body = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    difficult = models.IntegerField(choices=DIFFICULT_STAR)
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_last_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def short_body(self):
        if len(self.body) > 30:
            return f'{self.body[:30]}...'
        return self.body
