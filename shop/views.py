from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Checkout
from math import ceil

def index(request):
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category']for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])
    params={'allprods':allprods}
    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"shop/contact.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def productview(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodview.html", {'product':product[0]})

def checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip_code')
        phone=request.POST.get('phone')
        order=Checkout(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        print(f"name: {name}, email: {email}, address: {address}, city: {city}, state: {state}, zip_code: {zip_code}, phone: {phone}")

    return render(request,'shop/checkout.html')

