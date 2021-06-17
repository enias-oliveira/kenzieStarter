from django.db import models


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
