from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user=models.OneToOneField(User)

    profile_pic=models.ImageField(blank=True,upload_to='upload_pics')

    portfolio_link=models.URLField(blank=False)

    def __str__(self):
        return self.user.username
    