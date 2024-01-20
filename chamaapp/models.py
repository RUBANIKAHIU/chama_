from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    GENDER_CHOICES = (
        ('M' ,'Male'),
        ('F' ,'Female')
    )
    user=models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    profile_user_id=models.AutoField(primary_key=True, default=1 ,blank=False, null=False)
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    phone_number= models.IntegerField(unique=True,blank=False)
    email=models.EmailField(unique=True,blank=False,max_length=100)
    gender=models.CharField(max_length= 8, choices=GENDER_CHOICES)
    date_of_birth=models.DateField()

    def __str__(self):
        return self.first_name

class Login (models.Model):   
    user=models.OneToOneField(User,  default=1 ,on_delete=models.CASCADE)
    profile_user_id=models.AutoField(primary_key=True, default=1 ,blank=False,null=False)
    phone_number=models.IntegerField(unique=True,blank=False)

    def __str__(self):
        return self.phone_number