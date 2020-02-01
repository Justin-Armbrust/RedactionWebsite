from django.db import models

# Create your models here.
class History(models.Model):
    input = models.TextField(max_length = 2000)
    output = models.TextField(max_length = 2000)
    jsonResponse = models.TextField()

    def __str__(self):
        return self.output