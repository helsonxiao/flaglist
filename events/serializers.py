from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ('id', 'owner', 'url', 'priority', 'title', 'text', 'created_date', 'status', 'expire_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'url', 'events',)