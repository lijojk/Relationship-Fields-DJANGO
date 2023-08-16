# one to many
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pic_author/')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='books/covers/', blank=True, null=True)
    summary = models.TextField()

    def __str__(self):
        return self.title

