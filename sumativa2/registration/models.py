from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null= True, blank= True, upload_to="users")

    def __str__ (self) -> str:
        return f'{self.username}'