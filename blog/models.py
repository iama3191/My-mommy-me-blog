from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """Data model for recipe"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_recipes"
        )
    updated_on = models.DateTimeField(auto_now=True)
    ingredients = models.TextField()
    instructions = models.TextField(default="")
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """Sets the order of comments by date ascending"""
        ordering = ['-created_on']

    def __str__(self):
        """Return the title of the recipe"""
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Data model for comments"""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        """Sets the order of comments by date ascending"""
        ordering = ['created_on']

    def __str__(self):
        """Returns comment with body and name"""
        return f"Comment {self.body} by {self.name}"
