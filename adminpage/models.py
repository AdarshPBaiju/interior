from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    
    img = models.ImageField(upload_to='gallery/')
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.alt
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"