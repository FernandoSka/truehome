from django.db import models
from django.contrib.auth.models import User
from .validators import validate_m2


class Spot(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False)
    address = models.TextField(max_length = 50, null = False, blank = False)
    m2 = models.FloatField(validators=[validate_m2], null = False, blank = False)
    mail = models.EmailField(max_length = 50, null = False, blank = False)

# Create your models here.
