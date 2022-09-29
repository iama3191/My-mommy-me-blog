from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Recipe, Comment


class TestViews(TestCase):
    """
    Test blog app views
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
            ingredients='ingredients1',
            instructions='instructions1',
            description='Some content',
            status=1
        )

        self.comment = Comment.objects.create(
            recipe=self.recipe,
            name=self.user,
            body='test comment',
        )

    def test_get_about_page(self):
        """
        Test about retrieval and correct template used
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_recipe_list_page(self):
        """Test blog retrieval and correct template used"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html', 'index.html')

    def test_get_add_recipe_page(self):
        """Test blog retrieval and correct template used"""
        response = self.client.get(reverse('add_recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_get_update_recipe_page(self):
        """Test blog retrieval and correct template used"""
        response = self.client.get(f'/update_recipe/{self.recipe.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_recipe.html')



