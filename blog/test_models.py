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

    def test_recipe_model_str_returns_name(self):
        """
        Test the __str__ method for recipe
        """
        self.assertEqual(self.recipe.__str__(), self.recipe.title)

    def test_comment_model_str_returns_name(self):
        """
        Test the __str__ method for comment
        """
        self.assertEqual(
            self.comment.__str__(),
            f"Comment {self.comment.body} by {self.comment.name}"
            )

    def test_comment_default_value(self):
        """
        Test default value for the comment
        """
        self.assertTrue(self.comment.approved)

    def test_recipe_default_value(self):
        """
        Test default value for the comment status
        """
        self.assertTrue(self.recipe.status == 0)
        
    def test_recipe_like_user(self):
        """Test likes counting"""
        testuser = User.objects.create_user(
            username='user1', password='12345'
        )
        testuser2 = User.objects.create_user(
            username='user2', password='123456'
        )
        title = Recipe.objects.create(
            title='cake', author=self.user
        )
        title.likes.set([testuser.pk, testuser2.pk])
        self.assertEqual(title.likes.count(), 2)