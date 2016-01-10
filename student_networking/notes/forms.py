from django.forms import ModelForm
from django import forms


class MultiTagField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""

        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')


class NoteForm(forms.Form):
    tags = MultiTagField()
    text = forms.Textarea()
