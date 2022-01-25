from django.db import models
from category.models import category

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=30)
    price=models.PositiveSmallIntegerField(default=0)
    description=models.TextField()
    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

