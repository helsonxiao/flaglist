# coding: utf-8-
from todolist import settings
from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('priority', 'title', 'text',)

    expire_date = forms.DateField(widget=forms.DateInput,
                                  input_formats=settings.DATE_INPUT_FORMATS, initial='yyyy-mm-dd(删除即不会过期)', required=False)

