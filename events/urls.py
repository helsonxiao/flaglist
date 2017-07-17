from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^unfinished/$', views.list_unfinished, name='list_unfinished'),
    url(r'^finished/$', views.list_finished, name='list_finished'),
    url(r'^all/$', views.list_all, name='list_all'),
    # ex: /7/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
]