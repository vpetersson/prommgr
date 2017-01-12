from django.contrib import admin
from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = (
        'server_ip',
        'cloudnet_owner_id',
        'cloudnet_server_id',
        'created_at',
        'updated_at',
        'deleted',
    )
    search_fields = (
        'cloudnet_owner_id',
        'cloudnet_server_id',
        'server_ip',
    )
    list_filter = (
        'created_at',
        'deleted',
    )
    ordering = ('-created_at',)

admin.site.register(Server, ServerAdmin)
