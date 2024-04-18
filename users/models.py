from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    """
    Defines a custom user model 
    extending Django's AbstractUser. 
    """

    STATUS = (
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Advanced'),
    )

    email = models.EmailField(unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    bio = models.TextField(max_length=600, default='', blank=True)
    profile_image = CloudinaryField('image', default='profile_image_placeholder.png')

    def __str__(self):

        return f'{self.username}'
