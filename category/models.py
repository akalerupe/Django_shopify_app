from django.db import models

# Create your models here.
class Category (models.Model):
    name=models.CharField(max_length=50)

    @staticmethod
    # a regular function defined inside a class that doesnt have access to the instance thus can be called without instantiating
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
