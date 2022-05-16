from django.db import models

# Create your models here.
DURATION_CHOICES = (("Days", "Days"), ("Month", "Month"), ("Year", "Year"))
class Member(models.Model):
    name =  models.CharField(max_length=20)
    gender =  models.CharField(max_length=10)
    date_of_birth = models.DateField()
    contact = models.CharField(max_length=20)
    duration = models.IntegerField(null=True, blank=True)
    duration_type = models.CharField(max_length=100, choices=DURATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name