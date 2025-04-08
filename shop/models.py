from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=300)
    category=models.CharField(max_length=200,default="")
    subcategory=models.CharField(max_length=200,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
    

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=200,default="")
    phone=models.IntegerField()
    desc=models.CharField(max_length=400,default="")

    def __str__ (self):
        return self.name
    


class Checkout(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=111)
    name=models.CharField(max_length=111)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111,default="")



