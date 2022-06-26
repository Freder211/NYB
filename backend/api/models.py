from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.


class Crew(models.Model):
    users = models.ManyToManyField(User, through="Membership", related_name="crews")


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "crew"]


class CrewContentModel(models.Model):
    title = fields.CharField(max_length=50, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, null=True)
    datetime_created = fields.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["datetime_created"]


class Communication(CrewContentModel):
    content = fields.TextField(blank=True)
    date_published = fields.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Schema(CrewContentModel):
    description = fields.TextField(blank=True)
    image = models.FileField(blank=True, upload_to="schemas/")
    date_published = fields.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class TodoList(CrewContentModel):
    def done_count(self):
        aggreagtion = self.items.filter(state=True).aggregate(items=Count("id"))
        return aggreagtion["items"]

    def undone_count(self):
        aggreagtion = self.items.filter(state=False).aggregate(items=Count("id"))
        return aggreagtion["items"]


class CrewChildContent(models.Model):
    @classmethod
    def get_parent_field(cls):
        p_field = cls.CrewMeta.parent_field
        if not isinstance(p_field, str):
            raise ValueError(
                "You must provide parent_field attribute in CrewMeta class and it must be a string."
            )
        return p_field

    @property
    def parent(self):
        return getattr(self, self.get_parent_field())

    class Meta:
        abstract = True

    class CrewMeta:
        parent_field = None


class TodoItem(CrewChildContent):
    tdlist_id = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, related_name="items"
    )
    state = fields.BooleanField(default=False)
    content = fields.TextField(blank=True)

    class CrewMeta:
        parent_field = "tdlist_id"
