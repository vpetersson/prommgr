from django.contrib.auth.models import User
from django.http import Http404
from lib import prom_helper
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.models import Server
from restapi.serializers import ServerSerializer
from restapi.serializers import UserSerializer


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


class ServerByOwner(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, request, owner):
        try:
            return Server.objects.filter(cloudnet_owner_id=owner)
        except Server.DoesNotExist:
            raise Http404

    def get(self, request, owner, format=None):
        servers = self.get_object(request, owner)
        serializer = ServerSerializer(servers, many=True)
        return Response(serializer.data)


class PromServerConfig(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Server.objects.get(pk=pk)
        except Server.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        server = self.get_object(pk)

        serializer = ServerSerializer(server)
        payload = prom_helper.generate_prom_server_config(serializer.data)
        return Response(payload)
