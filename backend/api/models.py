from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User

# Create your models here.

class ModelOwnership(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

class Communication(ModelOwnership):
    title = fields.CharField(max_length=50, blank=True)
    content = fields.TextField(blank=True)
    date_published = fields.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Schema(ModelOwnership):
    title = fields.CharField(max_length=50, blank=True)
    description = fields.TextField(blank=True)
    image = models.FileField(blank=True, upload_to="schemas/")
    date_published = fields.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
