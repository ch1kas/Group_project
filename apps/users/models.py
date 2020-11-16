from django.contrib.auth.models import AbstractUser
from django.db import models
import os
import random


def get_filename_extension(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 9999999999)
    name, ext = get_filename_extension(filename)
    final_converted_name = f"{new_filename}{ext}"
    return f"avatars/{new_filename}/{final_converted_name}"




class User(AbstractUser):
    is_volunteer = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    # date_joined = models.DateField(auto_now_add=True)
    bio = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    # date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)


    def __str__(self):
        return f'{self.name}'

