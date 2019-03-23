from django import forms
from django.core import validators
class FormName(forms.Form):
    name=forms.CharField(max_length=264,validators=[validators.MaxLengthValidator(3)])
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        b=self.cleaned_data['name']
        if len(b)>5:
            raise forms.ValidationError("BootError")
        return b

