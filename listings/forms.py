# myapp/forms.py
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
