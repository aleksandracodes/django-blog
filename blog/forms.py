from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)  # comma is important, otherwise Python will read it as a string instead of a tuple
