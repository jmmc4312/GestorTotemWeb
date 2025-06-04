# forms.py
from django import forms

class TotemValidationForm(forms.Form):
    code_part1 = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'maxlength': '3'}))
    code_part2 = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'maxlength': '3'}))
    code_part3 = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'maxlength': '3'}))
