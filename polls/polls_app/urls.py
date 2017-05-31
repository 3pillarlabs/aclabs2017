from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[-_\w\s]+)/$', views.detail, name='detail'),
]
