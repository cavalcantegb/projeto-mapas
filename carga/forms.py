from django import forms
from django.forms import ClearableFileInput
from .types import table_type


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=ClearableFileInput(attrs={'multiple': True}))
    table = forms.ChoiceField(choices=table_type, widget=forms.RadioSelect, initial=table_type[1], required=True)

