from todolist import settings
from .models import Event
from django import forms
from .models import PRIORITY_CHOICES


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'text',)

    expire_date = forms.DateField(widget=forms.DateInput,
                                  input_formats=settings.DATE_INPUT_FORMATS, initial='yyyy-mm-dd')
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
