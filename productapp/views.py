from django.shortcuts import render
from productapp.models import Product
from django.contrib import humanize

# Create your views here.



def index(request):
    product=Product.objects.filter(isTrending=True)
    return render(request,'index.html',{'product':product})
                  
    
    
    

def details(request,id):
    product=Product.objects.get(id=id)

    
    return render(request,'details.html',
                  {
                      
                      'product':product
                  }
                  )    
