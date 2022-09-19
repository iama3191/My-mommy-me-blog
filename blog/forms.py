"""
Forms
"""
from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'description',
            'ingredients',
            'instructions',
            'featured_image',
        ]
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget()
        }