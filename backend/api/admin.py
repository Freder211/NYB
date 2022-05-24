from django.contrib import admin
from django.contrib.admin.options import TabularInline
from api.models import Communication, Crew, Schema, Membership


class ModelOwnershipAdmin(admin.ModelAdmin):
    exclude = ("author",)

    def get_queryset(self, request):
        user = request.user
        user_crews = user.crews.all()
        return super().get_queryset(request).filter(crew__in=user_crews)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Communication)
class CommunicationAdmin(ModelOwnershipAdmin):
    pass


@admin.register(Schema)
class SchemaAdmin(ModelOwnershipAdmin):
    pass


class MembershipInline(TabularInline):
    extra = 0
    model = Membership


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            return

        u = request.user
        u.crews.add(obj)
        u.save()
