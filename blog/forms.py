from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """Form for comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        fields = ('name','email','body')
