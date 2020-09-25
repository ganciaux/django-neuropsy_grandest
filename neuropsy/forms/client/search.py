from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email')