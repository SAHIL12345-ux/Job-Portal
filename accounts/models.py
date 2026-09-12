
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('jobseeker', 'Job Seeker'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='jobseeker'
    )

    def __str__(self):
        return self.username
