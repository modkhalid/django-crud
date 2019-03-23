from django import forms

class FormName(forms.Form):
    name=forms.CharField(max_length=264)
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        b=self.cleaned_data['name']
        if len(b)>5:
            raise forms.ValidationError("BootError")
        return b

