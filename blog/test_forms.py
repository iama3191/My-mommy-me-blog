from django.test import TestCase
from .forms import CommentForm, RecipeForm


class TestCommentForm(TestCase):
    """Test the forms"""

    def test_message_is_required(self):
        """Test that the body field from the comment form is valid"""
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_forms_metaclass(self):
        """
        Testing the meta class
        """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestRecipeForm(TestCase):
    """Test the recipe form"""

    def test_fields_are_required(self):
        """Test that the field from the recipe form are valid"""
        form_recipe = RecipeForm({'title': ''})
        self.assertFalse(form_recipe.is_valid())
        self.assertIn('title', form_recipe.errors.keys())
        self.assertEqual(form_recipe.errors['title'][0], 'This field is required.')
        