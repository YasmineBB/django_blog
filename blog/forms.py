from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        # error_messages = {
        #     'body': {
        #         "required": ("No task added!"),
        #         'max_length': ("Maximum length limit: 10 characters!"),
        #     },
        # }