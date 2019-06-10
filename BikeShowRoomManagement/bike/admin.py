from django.contrib import admin
from bike.models import Bike
from booking.models import Booking
from customer.models import Customer
from insurance.models import Insurance
from repair_bike.models import Repair_Bike
# Register your models here.

admin.site.register(Bike)
admin.site.register(Booking)
admin.site.register(Customer)
admin.site.register(Insurance)
admin.site.register(Repair_Bike)