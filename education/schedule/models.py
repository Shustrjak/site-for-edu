from django.db import models

class Schedule(models.Model):
    GROUP = (
        (1, 'garden'),
        (2, 'farm'),
        (3, 'animal'),
        (4, 'pets'),
    )
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    group = models.IntegerField(choices=GROUP)

    def __str__(self):
        return self.title
