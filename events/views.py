from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Event


def index(request):
    return render(request, 'events/index.html')


def list_unfinished(request):
    events = Event.objects.filter(status=False).order_by('-created_date')
    context = {'events': events}
    return render(request, 'events/unfinished.html', context)


def list_finished(request):
    events = Event.objects.filter(status=True).order_by('-created_date')
    context = {'events': events}
    return render(request, 'events/finished.html', context)


def list_all(request):
    events = Event.objects.all().order_by('-created_date')
    context = {'events': events}
    return render(request, 'events/all.html', context)


def detail(request, event_id):
    content = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'content': content})