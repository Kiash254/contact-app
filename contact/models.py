from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname=models.CharField(max_length=100,null=True,blank=True)
    relationship=models.CharField(max_length=100)
    email=models.EmailField(max_length=254,null=True,blank=True)
    phone_no=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.fullname