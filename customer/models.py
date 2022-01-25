import email
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.models.PhoneNumberField(unique = True, null = False, blank = False)
    email=models.EmailField()
    password=models.CharField()

    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email():
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
        


