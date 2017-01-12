from rest_framework import serializers
from restapi.models import Server
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    server = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Server.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'server')


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = (
            'cloudnet_owner_id',
            'cloudnet_server_id',
            'comment',
            'created_at',
            'deleted',
            'id',
            'server_ip',
            'updated_at',
        )
