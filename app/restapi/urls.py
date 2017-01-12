from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    url(r'^servers$', views.ServerList.as_view()),
    url(r'^servers/(?P<pk>[0-9]+)/$', views.ServerDetail.as_view()),
    url(
        r'^server-by-ip/(?P<server_ip>(?:[0-9]{1,3}\.){3}[0-9]{1,3})/$',
        views.ServerByIp.as_view()
    ),
    url(
        r'^server-by-owner/(?P<owner>[0-9]+)/$',
        views.ServerByOwner.as_view()
    ),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
