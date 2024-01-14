from .models import Purchases
from django.db.models.signals import post_save

from django.dispatch import receiver

@receiver(post_save, sender=Purchases)
def update_product_stock(sender, instance, created, **kwargs):
    """
    Signal to update the stock in the Product table after a new purchase is created.
    """
    if created:
        brand = instance.brand
        product = instance.product
        if product.brand == brand:            
            quantity_purchased = instance.quantity
        
            if product.stock is None:
                product.stock = 0

            product.stock += quantity_purchased
            product.save()