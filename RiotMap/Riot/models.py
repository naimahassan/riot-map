from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User=get_user_model()


class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='images/',blank=True)
    bio=models.TextField()
    user=models.ForeignKey(User)
    def __str__(self):
        return self.bio
    @classmethod
    def my_profile(cls,user_id):
        profiles=Profile.objects.get(id=user_id)

        return profiles

class Post(models.Model):
    name=models.CharField(max_length=60)
    riot_description=models.TextField(max_length=100)
    riot_area=models.CharField(max_length=100)
    Profile=models.ForeignKey(Profile)

    def __str__(self):
        return self.name



# Create your models here.
