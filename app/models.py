from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    long_description = models.TextField(default='')
    thumnail_image = models.ImageField(upload_to='images/product')
    price = models.IntegerField()
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Address(models.Model):
    id =models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.TextField(default="")
    state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    state = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)
    city = models.CharField(default="",max_length=20)
    pincode = models.IntegerField(blank=True)



class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, default=1)


    def __str__(self):
        return self.product.title

    def short_dsc(self):
        return self.product.short_description

    def price(self):
        return self.product.price
    
    def thumnail_image(self):
        return self.product.thumnail_image
    

class BuyOrders(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart ,on_delete=models.CASCADE)
    address = models.ForeignKey(Address ,on_delete=models.CASCADE)
    paymentMethod = models.CharField(max_length=50 , default='')

