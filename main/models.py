from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    phone = models.CharField(max_length=255, null=True, blank=True)
    is_client = models.BooleanField(default=True)
    is_call_center = models.BooleanField(default=False)
    is_cooker = models.BooleanField(default=False)
    is_deliver = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


