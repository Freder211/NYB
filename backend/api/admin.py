from django.contrib import admin
from api.models import Communication


@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)
