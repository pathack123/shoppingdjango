
from django.urls import path
from orderapp import views



urlpatterns = [
    path('order/',views.order),
    path('ordercomplete/',views.order),
    path('orderhistory/',views.orderHistory),
    path('orderdetails/<order_id>',views.orderDetail)
    
    
]
