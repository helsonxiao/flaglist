# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from events.permissions import IsOwnerOrReadOnly
from .models import Event
from .forms import EventForm
from .serializers import EventSerializer, UserSerializer
from rest_framework import generics, permissions, viewsets, filters
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend


class EventViewSet(viewsets.ModelViewSet):
    """
    Show all events. Or you can filter them.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('status', 'owner')
    ordering_fields = ('expire_date', 'priority')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# --------------------------------------------------
# 以下为 可视化API 精简过程中遗留的代码，仅供学习，待删除。

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'events': reverse('event-list', request=request, format=format)
#     })
#
#
# class EventList(generics.ListCreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('status',)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class EventDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('status',)
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# ------------
# 以下为耦合部分


def index(request):
    return render(request, 'events/index.html')


class AllEventView(generic.ListView):
    template_name = 'events/flaglist.html'
    context_object_name = 'events'
    status = False
    paginate_by = 3

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user, created_date__lte=timezone.now())


class EventListView(generic.ListView):
    template_name = 'events/flaglist.html'
    context_object_name = 'events'
    status = False
    paginate_by = 3

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user, status=self.status, created_date__lte=timezone.now())


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect('detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/edit.html', context={'form': form})


@login_required
def remove_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    status = event.status
    event.delete()
    if status:
        return redirect('list_finished')
    else:
        return redirect('list_unfinished')


@login_required
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)  # todo
            event.owner = request.user
            event.save()
            return redirect('detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit.html', context={'form': form})


@login_required
def finish_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.status = True
    event.save()
    return redirect('list_finished')


# ----------------------------------------------------
# 精简过程中被丢弃或者还有可能被用到的代码，仅供学习用，待删除。

# class UnfinishedListView(generic.ListView):
#     template_name = 'events/flaglist.html'
#     context_object_name = 'events'
#
#     def get_queryset(self):
#         return Event.objects.filter(owner=self.request.user, status=False, created_date__lte=timezone.now())


# def list_unfinished(request):
#     events = Event.objects.filter(owner=request.user, status=False, created_date__lte=timezone.now())
#     return render(request, 'events/flaglist.html', context={'events': events})


# class FinishedListView(generic.ListView):
#     template_name = 'events/flaglist.html'
#     context_object_name = 'events'
#
#     def get_queryset(self):
#         return Event.objects.filter(owner=self.request.user, status=True, created_date__lte=timezone.now())


# def list_finished(request):
#     events = Event.objects.filter(owner=request.user, status=True, created_date__lte=timezone.now())
#     return render(request, 'events/flaglist.html', context={'events': events})

# def list_all(request):
#     events = Event.objects.filter(owner=request.user, created_date__lte=timezone.now())
#     return render(request, 'events/flaglist.html', context={'events': events})

# @login_required
# def detail(request, pk):
#     event = get_object_or_404(Event, pk=pk)
#     return render(request, 'events/detail.html', context={'event': event})
