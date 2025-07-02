from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ein eines Usermodel. Muss in den Settings registriert werden:

    AUTH_USER_MODEL = 'user.CustomUser'
    """

    address = models.CharField(max_length=100, blank=True, null=True)
