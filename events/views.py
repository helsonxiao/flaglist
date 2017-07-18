from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db import models
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def index(request):
    return render(request, 'events/index.html')


@login_required
def list_unfinished(request):
    events = Event.objects.filter(user=request.user, status=False, created_date__lte=timezone.now()).order_by('-created_date')
    context = {'events': events}
    return render(request, 'events/FlagList.html', context)


@login_required
def list_finished(request):
    events = Event.objects.filter(user=request.user, status=True, created_date__lte=timezone.now()).order_by('-created_date')
    context = {'events': events}
    return render(request, 'events/FlagList.html', context)


@login_required
def list_all(request):
    events = Event.objects.filter(user=request.user, created_date__lte=timezone.now()).order_by('-created_date')
    context = {'events': events}
    return render(request, 'events/FlagList.html', context)


@login_required
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})


@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('detail', event_id=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/edit.html', {'form': form})

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
            event.user = request.user
            event.save()
            return redirect('detail', event_id=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit.html', {'form': form})