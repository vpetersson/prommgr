from django.db import models


class Server(models.Model):
    server_ip = models.GenericIPAddressField(
        verbose_name='Server IP'
    )
    server_port = models.IntegerField(
        verbose_name='Server Port',
        default=9100
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
