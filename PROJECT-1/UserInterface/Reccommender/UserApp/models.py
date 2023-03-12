from django.db import models



# Create your models here.
class UserInfo(models.Model):
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    email=models.EmailField()
    college=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class UserInfoDB(models.Model):
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    email=models.EmailField()
    college=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    