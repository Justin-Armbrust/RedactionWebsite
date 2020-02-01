from django.db import models

# Create your models here.
class History(models.Model):
    input = models.CharField(max_length = 2000)
    output = models.CharField(max_length = 2000)
    jsonResponse = models.TextField()

    def __str__(self):
        return self.input, self.output, self.jsonResponse