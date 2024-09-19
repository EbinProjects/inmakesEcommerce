from django.urls import path
from . import views

app_name = 'cart_app'
urlpatterns = [
    path('add/<int:product_id>', views.addToCart, name='addToCart'),
    path('minus/<int:product_id>', views.minusCart, name='minusCart'),
    path('remove/<int:product_id>', views.removeCart, name='removeCart'),
    path('', views.cart_Details, name='cart_Details')
]
