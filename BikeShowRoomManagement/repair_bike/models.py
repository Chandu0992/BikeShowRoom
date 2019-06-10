from django.db import models

# Create your models here.
class Repair_Bike(models.Model):
    repair_bike_id = models.CharField(primary_key=True,max_length=15)
    repair_bike_customer_id = models.CharField(max_length=50)
    repair_bike_number = models.CharField(max_length=20)
    repair_bike_bill = models.CharField(max_length=10)
    repair_bike_type = models.CharField(max_length=20)
    repair_bike_description = models.CharField(max_length=500)

    def __str__(self):
        return self.repair_bike_id