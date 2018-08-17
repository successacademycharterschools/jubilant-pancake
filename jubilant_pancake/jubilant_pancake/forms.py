"""Form for Jubilant Pancake project"""
from django import forms


class PancakeForm(forms.Form):
    """PancakeForm only needs two fields"""
    string_1 = forms.CharField()
    string_2 = forms.CharField()
