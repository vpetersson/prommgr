from django.db import models


class Server(models.Model):
    cloudnet_owner_id = models.IntegerField(
        verbose_name='Cloud.net Owner Id',
    )
    cloudnet_server_id = models.IntegerField(
        verbose_name='Cloud.net Server Id',
    )
    server_ip = models.GenericIPAddressField(
        verbose_name='Server IP'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    comment = models.CharField(
        max_length=250,
        blank=True
    )

    def __str__(self):
        return self.server_ip

    class Meta:
        ordering = ('-created_at',)
