from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


DURATION_CHOICES = (("Days", "Days"),("Week", "Week"), ("Month", "Month"), ("year", "Year"))
class Member(models.Model):
    name =  models.CharField(max_length=20)
    gender =  models.CharField(max_length=10)
    date_of_birth = models.DateField()
    contact = models.CharField(max_length=20)
    duration = models.IntegerField(null=True, blank=True)
    duration_type = models.CharField(max_length=100, choices=DURATION_CHOICES, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name