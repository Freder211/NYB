from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.base import Model

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


def generate_list_model(
    name: str, state_field_name: str, positive_count_name: str, negative_count_name: str
):
    def items_count(self, filter_data):
        aggreagtion = self.items.filter(**filter_data).aggregate(items=Count("id"))
        return aggreagtion["item"]

    def positive_count(self):
        filter_data = {state_field_name: True}
        return self.items_count(filter_data)

    def negative_count(self):
        filter_data = {state_field_name: False}
        return self.items_count(filter_data)

    CrewMeta = type("CrewMeta", (object,), {"state_field_name": state_field_name})

    return type(
        name,
        (CrewContentModel,),
        {
            "items_count": items_count,
            positive_count_name: positive_count,
            negative_count_name: negative_count,
            "CrewMeta": CrewMeta,
            "__module__": __name__,
        },
    )


TodoList = generate_list_model("TodoList", "state", "done_count", "undone_count")


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


def generate_item_model(name: str, list_model: CrewContentModel, fk_field: str):
    pass


class TodoItem(CrewChildContent):
    tdlist_id = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, related_name="items"
    )
    state = fields.BooleanField(default=False)
    content = fields.TextField(blank=True)

    class CrewMeta:
        parent_field = "tdlist_id"
