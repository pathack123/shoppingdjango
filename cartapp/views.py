from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from productapp.models import Product
from cartapp.models import Cart,CartItem

# Create your views here.
@login_required(login_url='/login')
def create_cartId(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    
    return cart    



@login_required(login_url='/login')
def cart(request):
    counter = 0
    total = 0
    try:
        cart= Cart.objects.get(cart_id=create_cartId(request))
        
        cartItem = CartItem.objects.filter(cart=cart)
        
        for item in cartItem:
            counter += item.quantity
            total += (item.product.price * item.quantity)
            
    except (Cart.DoesNotExist,CartItem.DoesNotExist):
        cart = None
        cartItem = None        
    
    return render(request,'cart.html',{'cartItem':cartItem,'total':total,'counter':counter})





@login_required(login_url='/login')
def deleteCart(request,id):
    cart=Cart.objects.get(cart_id=create_cartId(request),customer=request.user)
    product=Product.objects.get(id=id)
    CartItem.objects.get(cart=cart,product=product).delete()
    return redirect('/cart')
    
   






@login_required(login_url='/login')
def addCart(request,id):
    product = Product.objects.get(id=id)
    
    try:
        cart=Cart.objects.get(cart_id=create_cartId(request))
        
    except Cart.DoesNotExist:
        cart= Cart.objects.create(cart_id = create_cartId(request),customer=request.user)
        cart.save()
        
    try:
        cartitem = CartItem.objects.get(product = product,cart=cart)
        
        if cartitem.quantity < cartitem.product.stock:
            cartitem.quantity += 1
            cartitem.save()
            
        
    except CartItem.DoesNotExist:
        cartitem = CartItem.objects.create(product=product,cart=cart,quantity=1)
        cartitem.save()
        
    
    return redirect('/cart')            
            
    