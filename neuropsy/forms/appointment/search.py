from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms


class NameForm(forms.Form):
    date_from = forms.DateField(
        widget=DateTimePickerInput())
    date_to = forms.DateField(
        widget=DateTimePickerInput())