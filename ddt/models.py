from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Registration(models.Model):
    handle = models.CharField("Name / Handle", max_length=64)
    amount = models.IntegerField("People attending, including yourself", default=1, validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ])
    hidden = models.BooleanField("Hide name from listing", default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.handle


class Wall(models.Model):
    handle = models.CharField(max_length=64)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.handle


class SiteSettings(models.Model):
    registration_open = models.BooleanField(default=False)
    wall_open = models.BooleanField(default=False)
