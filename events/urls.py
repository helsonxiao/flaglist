from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from . import views

schema_view = get_schema_view(title='FlagList API')

router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # API View
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^api/$', views.api_root),
    # url(r'^api/events/$', views.EventList.as_view(), name='event-list'),
    # url(r'^api/events/(?P<pk>[0-9]+)/$', views.EventDetail.as_view(), name='event-detail'),
    # url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    # url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^api/', include(router.urls)),

    # Normal View
    url(r'^$', views.index, name='index'),
    url(r'^unfinished/$', views.EventListView.as_view(status=False), name='list_unfinished'),
    url(r'^finished/$', views.EventListView.as_view(status=True), name='list_finished'),
    url(r'^all/$', views.AllEventView.as_view(), name='list_all'),
    # ex: /7/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /7/edit/
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_event, name='edit_event'),
    # ex: /7/remove/
    url(r'^(?P<pk>[0-9]+)/remove/$', views.remove_event, name='remove_event'),
    url(r'^create/$', views.create_event, name='create_event'),
    url(r'^(?P<pk>[0-9]+)/finish/$', views.finish_event, name='finish_event'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
