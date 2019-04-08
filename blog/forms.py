from django import forms
from .models import Post,Comment


class postForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text')


        widgets={
            'title':forms.TextInput(attrs={
                'class':'text-input-class'
            }),
            'text':forms.TextInput(attrs={
                'class':'editable medium-editor-textarea'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
            'title':forms.TextInput(attrs={
                'class':'text-input-class'
            }),
            'text':forms.TextInput(attrs={
                'class':'editable medium-editor-textarea'
            })
        }