
from django.urls import path
from cartapp import views




urlpatterns = [
    path('cart/',views.cart),
    path('cart/add/<int:id>',views.addCart),
    path('cart/delete/<id>',views.deleteCart)
   

    
]