
from django.db import models
class Person(models.Model):
    pname = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.pname