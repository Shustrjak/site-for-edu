from django.db import models


class Schedule(models.Model):
    garden = 1
    farm = 2
    animal = 3
    pets = 4

    GROUP = (
        (garden, 'garden'),
        (farm, 'farm'),
        (animal, 'animal'),
        (pets, 'pets'),
    )
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    group = models.IntegerField(choices=GROUP)

    def __str__(self):
        return self.title
