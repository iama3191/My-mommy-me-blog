"""
Forms
"""
from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """
    Establish the required fields for the comment form
    """
    class Meta:
        model = Comment
        fields = ("body",)


class RecipeForm(forms.ModelForm):
    """
    Establish the required fields for the recipe form
    """
    class Meta:
        model = Recipe
        fields = [
            "title",
            "slug",
            "description",
            "ingredients",
            "instructions",
            "featured_image",
        ]
        widgets = {
            "ingredients": SummernoteWidget(),
            "instructions": SummernoteWidget()
        }
