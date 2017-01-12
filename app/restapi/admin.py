from django.contrib import admin
from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = (
        'server_ip',
        'cloudnet_server_id',
        'cloudnet_owner_id',
        'created_at',
        'updated_at',
        'deleted',
    )
    search_fields = (
        'cloudnet_server_id',
        'server_ip',
        'owner',
    )
    list_filter = (
        'created_at',
        'deleted',
    )
    ordering = ('-created_at',)

admin.site.register(Server, ServerAdmin)
