from django.contrib import admin
from api.models import Communication, Schema


class ModelOwnershipAdmin(admin.ModelAdmin):
    exclude = ('author',)

    def get_queryset(self, request):
        user = request.user
        return super().get_queryset(request).filter(author=user)

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
