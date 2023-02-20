from django import forms
from django.forms import TextInput, Textarea

class SQLQueryForm(forms.Form):
    sql_query = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': "form-control",
            'id': "sql_form"
        })
    )
    