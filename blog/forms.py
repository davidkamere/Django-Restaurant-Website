from .models import Comment, Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Write your name here.....'}),
            'comment': forms.Textarea(
                attrs={'placeholder': 'Enter your comments/words here....'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('header_image', 'title', 'content', 'extra_info', 'serving', 'ingredients', 'instructions', 'category')
        widgets = {
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
            'title': forms.TextInput(attrs={'placeholder': 'Post Title.....'}),
            'serving': forms.TextInput(attrs={'placeholder': 'Serving for the recipe.....'}),
                 
        }


