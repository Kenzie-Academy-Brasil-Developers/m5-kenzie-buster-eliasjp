from django.db import models

# Create your models here.
class Rating_choices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=Rating_choices.choices, default=Rating_choices.G)
    synopsis = models.TextField(null=True, default=None)
    added_by = models.EmailField()