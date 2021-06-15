from django.db import models

state_choices = (
    (SUCCEEDED, "successful"),
    (FAILED, "failed"),
    (CANCELED, )
    (LIVE, )
)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    backers = models.IntegerField()
    created_at = models.DateTimeField()
    deadline = models.DateTimeField()
    goal = models.DecimalField()
    pledged = models.DecimalField()
    usd_pledged = models.DecimalField()
    currency = models.CharField(max_length=3)
    launched_at = models.DateTimeField()
    state = models.CharField(max_length=255, choices=status_choices, default="AGENDADO")
