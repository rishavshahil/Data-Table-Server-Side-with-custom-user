from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from home.models import Category
# from django.utils.translation import ugettext_lazy
# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField( unique =True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=250, choices=(('Male', 'Male'), ('Female','Female')))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.first_name