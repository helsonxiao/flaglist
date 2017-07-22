from .models import Event
from django import forms


class EventForm(forms.ModelForm):  # todo
    class Meta:
        model = Event
        fields = ('title', 'text', 'expire_date', 'priority')
