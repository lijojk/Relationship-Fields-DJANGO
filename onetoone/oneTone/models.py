from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    contact_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.user.username
