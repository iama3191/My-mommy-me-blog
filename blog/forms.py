"""
Forms
"""
from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
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