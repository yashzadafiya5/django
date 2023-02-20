from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class CustomUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length = 254)
    date_of_birth = models.DateField(null=True, blank=True)
    primary_contact_number = models.CharField(validators=[RegexValidator(r'^\+?1?\d{9,15}$')], max_length=17, unique=True)
    secondary_contact_number = models.CharField(validators=[RegexValidator(r'^\+?1?\d{9,15}$')], max_length=17, blank=True)
    currency = models.CharField(max_length=3)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
