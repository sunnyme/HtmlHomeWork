from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
	name=models.CharField(max_length=20)
	food=models.ForeignKey("Food")


class Food(models.Model):
	f_name=models.CharField(max_length=20)
	f_price= models.CharField(max_length=10)
	f_spicy=models.CharField(max_length=2)
	f_detail=models.CharField(max_length=15)
