from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=False)
    contact_info = models.CharField(max_length=255)
    experience = models.IntegerField(null=True, blank=True)
