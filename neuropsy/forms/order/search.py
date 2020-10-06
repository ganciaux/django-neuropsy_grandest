from bootstrap_datepicker_plus import DateTimePickerInput
from neuropsy.models.timestamp import TimeStampedModel
from django import forms


class searchForm(forms.Form):
    date_from = forms.DateField(
        widget=DateTimePickerInput(format='%d-%m-%Y %H:%M'),
        initial=TimeStampedModel.get_first_month_day())
    date_to = forms.DateField(
        widget=DateTimePickerInput(format='%d-%m-%Y %H:%M'),
        initial=TimeStampedModel.get_last_month_day())
