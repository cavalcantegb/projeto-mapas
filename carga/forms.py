from django import forms
from .types import table_type


class UploadFileForm(forms.Form):
    file = forms.FileField()
    table = forms.ChoiceField(choices=table_type, widget=forms.RadioSelect, initial=table_type[0], required=True)

