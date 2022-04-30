from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User

# Create your models here.

class Communication(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = fields.CharField(max_length=50, blank=True)
    content = fields.TextField(blank=True)
    date_published = fields.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

