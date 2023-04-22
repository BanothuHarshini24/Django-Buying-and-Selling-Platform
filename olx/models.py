from django.db import models
# from datetime import datetime
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime,timedelta
from django.utils import timezone
User=get_user_model()
# Create your models here.
class signed(models.Model):
   full_name=models.CharField(max_length=100)
   username=models.CharField(max_length=100)
   email=models.CharField(max_length=100)
   phone_number=models.CharField(max_length=100)
   password=models.CharField(max_length=100)
   confirm_password=models.CharField(max_length=100)


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profileimg=models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    location=models.CharField(max_length=100,blank=True)

def __str__(self):
    return self.user.username


class post(models.Model):
    id_post=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='post_images')
    image2=models.ImageField(upload_to='post_images')
    image3=models.ImageField(upload_to='post_images')
    image4=models.ImageField(upload_to='post_images')
    image5=models.ImageField(upload_to='post_images')
    created_at=models.DateTimeField(default=datetime.now)
    price=models.IntegerField()
    description=models.TextField()
    likes=models.IntegerField(default=0)
    cart=models.IntegerField(default=0)
    location=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    bid_price=models.IntegerField()
    @property
    def duration(self):
        return timezone.now()-self.created_at
    
def __str__(self):
    return self.user

class wishlist(models.Model):
    username=models.CharField(max_length=100)
    post_id=models.CharField(max_length=100)

def __str__(self):
    return self.username

class cart(models.Model):
    username=models.CharField(max_length=100)
    post_id=models.CharField(max_length=100)

def __str__(self):
    return self.username

class verify_post(models.Model):
    id_post=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='post_images')
    image2=models.ImageField(upload_to='post_images')
    image3=models.ImageField(upload_to='post_images')
    image4=models.ImageField(upload_to='post_images')
    image5=models.ImageField(upload_to='post_images')
    created_at=models.DateTimeField(default=datetime.now)
    price=models.IntegerField()
    description=models.TextField()
    likes=models.IntegerField(default=0)
    cart=models.IntegerField(default=0)
    location=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    verification=models.BooleanField(default=True)
    bid_price=models.IntegerField()

class myorders(models.Model):
    username=models.CharField(max_length=100)
    post_id=models.CharField(max_length=100)

class week_bid(models.Model):
    username=models.CharField(max_length=100)
    post_id=models.CharField(max_length=100)

class reports(models.Model):
    username=models.CharField(max_length=100)
    post_id=models.CharField(max_length=100)
    seller=models.CharField(max_length=100)

class not_verify(models.Model):
    id_post=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='post_images')
    image2=models.ImageField(upload_to='post_images')
    image3=models.ImageField(upload_to='post_images')
    image4=models.ImageField(upload_to='post_images')
    image5=models.ImageField(upload_to='post_images')
    created_at=models.DateTimeField(default=datetime.now)
    price=models.IntegerField()
    description=models.TextField()
    likes=models.IntegerField(default=0)
    cart=models.IntegerField(default=0)
    location=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    verification=models.BooleanField(default=True)
    bid_price=models.IntegerField()