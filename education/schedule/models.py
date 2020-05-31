from django.db import models
# from education.teacher.models import Teacher
# Create your models here.


class Schedule(models.Model):
    GROUP = (
        (1, 'garden'),
        (2, 'farm'),
        (3, 'animal'),
        (4, 'pets'),
    )
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    # author = models.ForeignKey(Teacher.full_name, on_delete=models.PROTECT)
    group = models.IntegerField(choices=GROUP)

    def __str__(self):
        return self.title
