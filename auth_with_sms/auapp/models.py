from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProfileModel(models.Model):
	phone=models.CharField(max_length=10,unique=True)
	location=models.CharField(max_length=20)
	user=models.OneToOneField(User,on_delete=models.CASCADE)


	