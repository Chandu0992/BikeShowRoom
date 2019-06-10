from django.db import models

# Create your models here.
class Insurance(models.Model):
    insurance_id = models.CharField(primary_key=True,max_length=15)
    insurance_bike_id = models.CharField(max_length=15)
    insurance_number = models.CharField(max_length=15)
    insurance_date = models.CharField(max_length=10)
    insurance_expiry = models.CharField(max_length=10)
    insurance_amount = models.CharField(max_length=8)
    insurance_type = models.CharField(max_length=20)
    insurance_description = models.CharField(max_length=500)

    def __str__(self):
        return self.insurance_id