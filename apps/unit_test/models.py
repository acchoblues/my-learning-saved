from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=255)
    sound = models.CharField(max_length=255)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name
