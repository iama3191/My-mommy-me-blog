from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment


class TestAppModels(TestCase):
    """
    Test app models
    """

    def setUp(self):
        """
        Create data for testing
        """
        self.user = User.objects.create(username='testname')
        self.user.set_password('secret_password')
        self.user.save()

        self.recipe = Recipe.objects.create(
            title='test recipe',
            slug='test-recipe',
            author=self.user,
        )

        self.comment = Comment.objects.create(
            recipe=self.recipe,
            name=self.user,
            body='test comment',
        )

    def test_recipe_model_str(self):
        """
        Test the __str__ method for recipe
        """
        self.assertEqual(self.recipe.__str__(), self.recipe.title)

    def test_comment_model_str(self):
        """
        Test the __str__ method for comment
        """
        self.assertEqual(
            self.comment.__str__(),
            f"Comment {self.comment.body} by {self.comment.name}"
            )