from .models import Purchases
from django.db.models.signals import post_save

from django.dispatch import receiver

@receiver(post_save, sender=Purchases)
def update_product_stock(sender, instance, created, **kwargs):
    """
    Signal to update the stock in the Product table after a new purchase is created.
    """
    brand = instance.brand
    product = instance.product
    quantity_purchased = instance.quantity

    if created:
        if product.brand == brand:                 
            if product.stock is None:
                product.stock = 0

            product.stock += quantity_purchased
            product.save()
    
    if instance.pk is not None:
        if product.brand == brand:
            if product.stock is None:
                product.stock = 0
            old_quantity = product.stock
            quantity_changed = quantity_purchased - old_quantity     
    
            product.stock += quantity_changed 
            print(old_quantity)           
            product.save()