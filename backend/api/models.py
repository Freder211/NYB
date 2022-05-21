from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User

# Create your models here.


class Crew(models.Model):
    users = models.ManyToManyField(User, through="Membership", related_name="crews")


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "crew"]


class CrewContentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, null=True)
    datetime_created = fields.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["datetime_created"]


class Communication(CrewContentModel):
    title = fields.CharField(max_length=50, blank=True)
    content = fields.TextField(blank=True)
    date_published = fields.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Schema(CrewContentModel):
    title = fields.CharField(max_length=50, blank=True)
    description = fields.TextField(blank=True)
    image = models.FileField(blank=True, upload_to="schemas/")
    date_published = fields.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
