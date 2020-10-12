from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

    # WIDGETS
    # fields and classes correspond to the css classes
    widgets = {
        'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postconent'})
    }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

    widegets = {
        'author': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
    }
