from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment


class TestModels(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username='testname')
        self.user.set_password('1234')
        self.user.save()

        self.recipe = Recipe.objects.create(
            title='test recipe',
            slug='test-recipe',
            author=self.user,
        )

        self.comment = Comment.objects.create(
            recipe=self.recipe,
            author=self.user,
            body='test comment'
        ) 