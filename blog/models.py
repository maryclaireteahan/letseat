from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Database model for assigning categories to the recipes
    """

    CATEGORY_CHOICES = [
        (1, "Breakfast"),
        (2, "Lunch"),
        (3, "Dinner"),
        (4, "Dessert"),
        (5, "Snack"),
    ]

    name = models.CharField(max_length=80, choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        """
        Order categories by name
        """
        ordering = ['name']

    def __str__(self):
        """
        Returns string representation of an object
        """
        return self.name


class Recipe(models.Model):
    """
    Database model for creating recipe posts
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts',
                               limit_choices_to={'is_superuser': True})
    updated_on = models.DateTimeField(auto_now=True)
    ingredients = models.TextField(max_length=20000, default='ingredients')
    instructions = models.TextField(max_length=20000, default='instructions')
    featured_image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, default='image alt')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    class Meta:
        """
        Order posts from newest to oldest
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        Returns the total number of like on a post
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Database model for commenting on recipe posts
    """
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        """
        Order comments from oldest to newest
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Returns string representation of an object
        """
        return f'Comment {self.body} by {self.name}'
