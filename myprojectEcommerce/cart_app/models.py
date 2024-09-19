from django.db import models
from myapp.models import Product, Category


# Create your models here.

class Cart(models.Model):
    cart_ID = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'ShopCart'
        ordering = ('date_added',)

    def __str__(self):
        return '{}'.format(self.cart_ID)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    def subTotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.names} (x{self.quantity})'
