from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment


class TestModels(TestCase):

    def setUpTestData(self):
        self.user = User.objects.create(username='testname')
        self.user.set_password('abcd')
        self.user.save()