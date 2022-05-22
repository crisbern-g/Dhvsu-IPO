from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPicture(models.Model):
    user_picture = models.ImageField(upload_to='user_picture')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_picture')
