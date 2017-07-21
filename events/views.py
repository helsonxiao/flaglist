
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from events.permissions import IsOwnerOrReadOnly
from .models import Event
from .forms import EventForm

from .serializers import EventSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'events': reverse('event-list', request=request, format=format)
    })


def index(request):
    return render(request, 'events/index.html')


@login_required
def list_unfinished(request):
    events = Event.objects.filter(owner=request.user, status=False, created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'events/FlagList.html', context={'events': events})


@login_required
def list_finished(request):
    events = Event.objects.filter(owner=request.user, status=True, created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'events/FlagList.html', context={'events': events})


@login_required
def list_all(request):
    events = Event.objects.filter(owner=request.user, created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'events/FlagList.html', context={'events': events})


@login_required
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', context={'event': event})


@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect('detail', event_id=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/edit.html', context={'form': form})


@login_required
def remove_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    status = event.status
    event.delete()
    if status:
        return redirect('list_finished')
    else:
        return redirect('list_unfinished')


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)  # todo
            event.owner = request.user
            event.save()
            return redirect('detail', event_id=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit.html', context={'form': form})


@login_required
def finish_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.status = True
    event.save()
    return redirect('list_finished')