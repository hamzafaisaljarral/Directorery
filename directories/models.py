from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError



class Teachers(models.Model):
    """models for the teacher."""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='static/images',default='static/images/placeholder.jpg')
    Email_address = models.EmailField(unique=True,max_length=100)
    phone_number = models.CharField(max_length=200)
    room_number = models.CharField(max_length=200)
    subjects_taught = models.CharField(max_length=200)
    def clean(self):
        sub=self.subjects_taught
        if (len(sub.split(',')) > 5 and self.pk is None):
            raise ValidationError('you can add 5 or less than 5 subjects')
    
    def __str__(self):
        return self.last_name
