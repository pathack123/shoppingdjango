from django.db import models
from django.contrib.auth.models import User
from productapp.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=50,blank=True)
    customer = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    
    
class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart =  models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    
    
       
