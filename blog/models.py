from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS =((0, 'Draft'), (1, 'Published'))

""" 
Database model for assigning categories to the recipes
"""
class Category(models.Model):

    """
    The categories to be assigned to the recipes
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
    """
    Order categories by name
    """ 
    class Meta:
        ordering = ['name']
    """ 
    Returns string representation of an object
    """
    def __str__(self):
        return self.name    

""" 
Database model for creating recipe posts
"""
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    ingredients = models.TextField(max_length=10000, null=True, blank=True)
    instructions= models.TextField(max_length=10000, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, null=True, blank=True)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)    

    """
    Order posts from newest to oldest
    """  
    class Meta:
        ordering = ['-created_on']
        
    """ 
    Returns string representation of an object
    """
    def __str__(self):
        return self.title

    """ 
    Returns the total number of like on a post
    """
    def number_of_likes(self):
        return self.likes.count()


""" 
Database model for commenting on recipe posts
"""
class Comment(models.Model):
    
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to associate the comment with a user

    

    """
    Order comments from oldest to newest
    """ 
    class Meta:
        ordering = ['created_on']
        
    """ 
    Returns string representation of an object
    """
    def __str__(self):
        return f'Comment {self.body} by {self.name}'
