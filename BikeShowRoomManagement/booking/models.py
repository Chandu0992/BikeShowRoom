from django.db import models

# Create your models here.
class Booking(models.Model):
    booking_id = models.CharField(primary_key=True,max_length=15)
    booking_title = models.CharField(max_length=50)
    booking_type = models.CharField(max_length=20)
    booking_date = models.CharField(max_length=10)
    booking_description = models.CharField(max_length=500)

    def __str__(self):
        return self.booking_id