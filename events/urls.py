from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # API View
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^api/$', views.api_root),
    # url(r'^api/events/$', views.EventList.as_view(), name='event-list'),
    # url(r'^api/events/(?P<pk>[0-9]+)/$', views.EventDetail.as_view(), name='event-detail'),
    # url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    # url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^api/', include(router.urls)),

    # Normal View
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

# urlpatterns = format_suffix_patterns(urlpatterns)