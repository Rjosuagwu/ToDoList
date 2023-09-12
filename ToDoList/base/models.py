from django.db import models
""" Deals with all of the authentication and things like the Username PassWord and Email
which allows us to pull various pieces of information to use in our application"""
from django.contrib.auth.models import User 
# Create your models here.
# Each attribute will be its own column in the database table this model creates
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150) 
    #CharField commonly used for names, Titles, small pieces of text
    description = models.TextField(null=True, blank=True)
    #Used for larger pieces of text 
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    """The following code is used to ensure readable text is outputted when an instance
    of the object is created, It allows the code to search for the "title" and use it"""
    def __str__(self):
        return self.title
    
    #following code is used to set the default ordering of the objects

    class Meta:
        ordering = ['complete']