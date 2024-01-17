from .models import Purchases, Sales
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from rest_framework.response import Response

############################ PURCHASES ###############################################
# Update stock of Product after new Purchase is created. 
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
    
    # elif instance.pk is not None:
    #     if product.brand == brand:
    #         if product.stock is None:
    #             product.stock = 0
    #         old_quantity = product.stock
    #         quantity_changed = quantity_purchased - old_quantity     
   
# Update stock of Product after existing Purchase is updated.
@receiver(pre_save, sender=Purchases)
def store_old_quantity(sender, instance, **kwargs):
    
    brand = instance.brand
    product = instance.product
    quantity_purchased = instance.quantity

    if instance.pk is not None:
        if product.brand == brand:
            old_instance = Purchases.objects.get(pk=instance.pk)
            if old_instance.quantity is not None:
                old_quantity = old_instance.quantity
            else:
                old_quantity = 0
            
            quantity_changed = quantity_purchased - old_quantity
    else:
        quantity_changed = quantity_purchased

    product.stock += quantity_changed        
    product.save() 

# Update stock of Product after existing Purchase is deleted.
@receiver(pre_delete, sender=Purchases)
def update_product_stock_on_delete(sender, instance, **kwargs):

    product = instance.product
    brand = instance.brand
    quantity_purchased = instance.quantity

    if product.brand == brand:
        product.stock -= quantity_purchased
        product.save()

    def delete(self, request, *args, **kwargs):
        return Response({"message": "This category deleted successfully!"})

############################ SALES ###############################################
# Update stock of Product after new Sales is created.  
@receiver(post_save, sender=Sales)
def update_product_stock(sender, instance, created, **kwargs):
    """
    Signal to update the stock in the Product table after a new stock is created.
    """
    brand = instance.brand
    product = instance.product
    quantity_saled = instance.quantity

    if created:
        if product.brand == brand:
            # Initial case                 
            if product.stock is None:
                product.stock = 0
            
            # If stock of product is greater or equal to quantity of sales
            if product.stock >= instance.quantity:
                product.stock -= quantity_saled
                product.save()
      