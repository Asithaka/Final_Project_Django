from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# this is user profile
#
class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=300, blank=True)
    dob = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship with user and profile
    friends = models.ManyToManyField(User, blank=True, related_name='friends') # user can have many friends
    created = models.DateTimeField(auto_now=True) # the date that profile was created
    updated = models.DateTimeField(auto_now_add=True) # the date that profile was updated

    def __str__(self):
        return f'{self.user.username}' # return the username of the user
    
STATUS_CHOICES = (
    ('sent', 'sent'),
    ('accepted', 'accepted'),
)

# this help to establishe the relation between two profiles
class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender') # user who send the freind requests
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver') # someone elese who reciving freind request
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="sent") # once they accept the frend request, status get updated as accepted
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

# This is about post

class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE) # check who is making this post
    image = models.ImageField(upload_to='images', blank=True) # need to install pillow
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    

# 
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # comment that associate to post
    username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE) # who is commenting
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True, blank=True) # date that commet was added

    def __str__(self):
        return self.text
    
class Like(models.Model):
    username = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE) # who liked it
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE) # what post they like it

   