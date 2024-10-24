from django.db import models

# Create your models here.
class contact_db(models.Model):
    Name = models.CharField(max_length=30,null=True,blank=True)
    Email_id = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=80,null=True,blank=True)

class register_db(models.Model):
    Username = models.CharField(max_length=30,null=True,blank=True)
    Email_id = models.CharField(max_length=50,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Password = models.CharField(max_length=30,null=True,blank=True)

class cart_db(models.Model):
    Username = models.CharField(max_length=30,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Product = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=150,null=True,blank=True)
    Size = models.CharField(max_length=30,null=True,blank=True)
    Color = models.CharField(max_length=30,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Total_price = models.IntegerField(null=True,blank=True)