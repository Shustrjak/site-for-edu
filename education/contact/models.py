from django.db import models


class Feedback(models.Model):
    input_name = models.CharField(max_length=255)
    input_mail = models.EmailField()
    input_text = models.CharField(max_length=255)
    copy = models.BooleanField(default=True)

