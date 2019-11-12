from django.contrib.auth.models import AbstractUser
from django.db import models

from clowning_around.users.models import Client, Clown

Rating_Choices = (
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "Good"),
        (4, "Very Good"),
        (5, "Excellent"),

    )
Status_choices = [
    'upcoming',
    'incipient',
    'completed',
    'cancelled',
]

class Appointment(models.Model):
    client = models.ManyToManyField(Client, on_delete=models.CASCADE)
    clown = models.ManyToManyField(Clown, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    rating = models.IntegerField(null=True, choices=Rating_Choices)
    status = models.CharField(max_length=20, choices=Status_choices, default='upcoming')
    issue = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.clown