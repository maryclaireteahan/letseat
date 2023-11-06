from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS =((0, 'Draft'), (1, 'Published'))



""" 
Database model for creating recipe posts
"""
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
   

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

class Comment(models.Model):
    
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
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
    


    