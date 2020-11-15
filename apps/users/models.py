from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
import os

from time import time



def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

def get_filename_extension(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = gen_slug('image')
    name, ext = get_filename_extension(filename)
    final_converted_name = f"{new_filename}{ext}"
    return f"avatars/{new_filename}/{final_converted_name}"




class User(AbstractUser):
    is_volunteer = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.SmallIntegerField()
    email = models.EmailField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True)
    USERNAME_FIELD = 'username'


    class Meta:
        db_table = "volunteer"



class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone_number = models.SmallIntegerField()
    email = models.EmailField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True)
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = "organization"


