from django.db import models
from django.utils.text import slugify
import os
from django.contrib.auth import get_user_model
from time import time

User = get_user_model()

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

def get_filename_extension(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = gen_slug('image')
    name, ext = get_filename_extension(filename)
    final_converted_name = f"{new_filename}{ext}"
    return f"avatars/{new_filename}/{final_converted_name}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts', null=True )
    image = models.ImageField(upload_to=upload_image_path, null=True)

