from django.contrib import admin
from . models import Product,Contact,Checkout


# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Checkout)