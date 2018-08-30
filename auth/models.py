from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    is_person_assigned = models.BooleanField(default=0)

