from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Write your name here.....'}),
            'comment': forms.Textarea(
                attrs={'placeholder': 'Enter your comments/words here....'}),
        }


# class PostForm(forms.ModelForm):
    # class Meta:
        # model = Post
        # fields = ('title', 'text')
        # widgets = {
            # 'title': forms.TextInput(attrs={'placeholder': 'Post Title.....'}),
            # 'text': forms.Textarea(
                # attrs={'placeholder': 'Enter your thoughts/words here....'}),
        # }


