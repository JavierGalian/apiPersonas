from django.db import models
from .validators import validate_password_strength
from django.contrib.auth.hashers import Argon2PasswordHasher, make_password
from django.contrib.auth.models import User
# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    name_user = models.CharField(max_length=200, null=False, blank=False,unique=True)
    email = models.EmailField(max_length=200 , null=False ,unique=True, blank=False)
    date_birth = models.DateField(null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False, default='', 
                                validators=[validate_password_strength])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password, hasher=Argon2PasswordHasher())
        super().save(*args, **kwargs)