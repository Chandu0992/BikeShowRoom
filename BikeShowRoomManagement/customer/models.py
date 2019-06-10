from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(primary_key=True,max_length=15)
    customer_name = models.CharField(max_length=50)
    customer_mobile = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=150)
    customer_username = models.CharField(max_length=50)
    customer_password = models.CharField(max_length=256)
    customer_address = models.CharField(max_length=500)
    
    def __str__(self):
        return self.customer_id
