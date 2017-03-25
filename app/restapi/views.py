from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.models import Server
from restapi.serializers import ServerSerializer
from restapi.serializers import UserSerializer
from rest_framework.exceptions import ValidationError


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.filter(deleted=False)
    serializer_class = ServerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        queryset = Server.objects.filter(
            server_ip=self.request.data['server_ip']
        )
        if queryset.exists():
            raise ValidationError("A server with this IP already exists."
                                  "Please delete the old one first.")
        serializer.save()


class ServerDetail(generics.RetrieveDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class ServerByIp(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, request, server_ip):
        try:
            return Server.objects.get(server_ip=server_ip)
        except Server.DoesNotExist:
            raise Http404

    def get(self, request, server_ip, format=None):
        server = self.get_object(request, server_ip)
        serializer = ServerSerializer(server)
        return Response(serializer.data)
