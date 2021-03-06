from django import forms
from django.forms import widgets


class HostBookForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Имя', widget=widgets.TextInput(
        attrs={'placeholder':'Name'}))
    email = forms.EmailField(max_length=200, required=True, label='Email', widget=widgets.TextInput(
        attrs={'placeholder':'Email'}))
    text = forms.CharField(max_length=3000, required=True, label='Текст',
                           widget=widgets.Textarea)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200, required=True, label='Поиск')