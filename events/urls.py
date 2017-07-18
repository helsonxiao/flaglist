from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^unfinished/$', views.list_unfinished, name='list_unfinished'),
    url(r'^finished/$', views.list_finished, name='list_finished'),
    url(r'^all/$', views.list_all, name='list_all'),
    # ex: /7/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /7/edit/
    url(r'^(?P<event_id>[0-9]+)/edit/$', views.edit_event, name='edit_event'),
    # ex: /7/remove/
    url(r'^(?P<event_id>[0-9]+)/remove/$', views.remove_event, name='remove_event'),
    url(r'^create/$', views.create_event, name='create_event'),
    url(r'^(?P<event_id>[0-9]+)/finish/$', views.finish_event, name='finish_event'),
]