from django.conf.urls import include, url
from . import views

urlpatterns= [
        url(r'^$', views.listar_publicacion),
        url(r'^postear/(?P<pk>[0-9]+)/$', views.post_detail, name='postear'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,  name='post_detail'),
        url(r'^postear/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
