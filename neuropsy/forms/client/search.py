from bootstrap_datepicker_plus import DatePickerInput
from django import forms


class searchForm(forms.Form):
    first_name = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email')
