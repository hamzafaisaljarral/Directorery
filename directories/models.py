from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class Teachers(models.Model):
    """models for the teacher."""
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=100)
    Profile_picture = models.ImageField(upload_to='static/images',default='static/images/placeholder.jpg')
    Email_Address = models.EmailField(unique=True,max_length=100)
    Phone_Number = models.CharField(max_length=200)
    Room_Number = models.CharField(max_length=200)
    Subjects_taught = models.CharField(max_length=200,null=True)
    def clean(self):
        sub=self.Subjects_taught
        if (len(sub.split(',')) > 5 and self.pk is None):
            raise ValidationError('you can add 5 or less than 5 subjects')
        
    
    def __str__(self):
        return self.Last_Name
