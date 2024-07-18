from django import forms
from .models import Video_model, Comment, User


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video_model
        fields = ['video_title', 'video_content', 'user', 'like', 'dislike']


class UserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['user_name', 'phone_number', 'email', 'password', 'password2']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'comment_user', 'video']