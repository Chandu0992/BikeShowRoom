from django.shortcuts import render
from booking.models import Booking

# Create your views here.

def showBooking(request,modify_res=None):
    return render(request, 'booking/add_booking.html', {'res':modify_res})

def addBooking(request):
    booking_id = request.POST.get('booking_id')
    booking_title = request.POST.get('booking_title')
    booking_type = request.POST.get('booking_type')
    booking_date = request.POST.get('booking_date')
    booking_desc = request.POST.get('booking_desc')
    add_booking = Booking(booking_id=booking_id,booking_title=booking_title,booking_type=booking_type,booking_date=booking_date,booking_description=booking_desc)
    add_booking.save()
    return showBooking(request)

def showEditBooking(request,msg=None):
    rec = Booking.objects.all()
    return render(request, 'booking/edit_booking.html', {'my_rec':rec, 'msg':msg})

def editBooking(request,msg=None):
    booking_id = request.POST.get('booking_id')
    update_data = Booking.objects.filter(booking_id = booking_id)
    res = list(update_data)[0]
    return showBooking(request,modify_res=res)

def deleteBooking(request):
    booking_id = request.POST.get('booking_id')
    Booking.objects.filter(booking_id = booking_id).delete()
    return showEditBooking(request, msg='Delete Booking Successfully')

def searchBooking(request):
    pid = request.POST.get('booking_id')
    search_data = Booking.objects.filter(booking_id=pid)
    res = list(search_data)[0]
    return show_searchBooking(request,modify_res=res)

def show_searchBooking(request,modify_res=None):
    return render(request, 'booking/search_booking.html', {'res':modify_res})