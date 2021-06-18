from django.db import models

from categories.models import Subcategory
from locations.models import Location
from creators.models import Creator


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    backers = models.IntegerField()
    created_at = models.DateTimeField()
    deadline = models.DateTimeField()
    goal = models.FloatField()
    pledged = models.FloatField()
    usd_pledged = models.FloatField()
    currency = models.CharField(max_length=3)
    launched_at = models.DateTimeField()
    state = models.CharField(max_length=255)
    state_changed_at = models.DateTimeField(null=True)

    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name="projects",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="projects",
    )
    creator = models.ForeignKey(
        Creator,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
