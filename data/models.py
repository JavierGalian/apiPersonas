from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    name_user = models.CharField(max_length=50, null=False, unique=True, blank=False)
    email = models.EmailField(max_length=200 , null=False ,unique=True, blank=False)
    date_birth = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
