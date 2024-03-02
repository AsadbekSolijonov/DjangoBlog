from django import forms

from blog.models import Comment, ClientInfo


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message', ]
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your comment here'}),
        }


class ClientInfoForm(forms.ModelForm):
    class Meta:
        model = ClientInfo
        fields = ['user', 'email', 'phone_number', 'message']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Enter phone number'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your comment here'}),
        }
