from django import forms

class SearchForm(forms.Form):
    text_input = forms.CharField()