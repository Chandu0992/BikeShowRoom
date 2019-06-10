from django.shortcuts import render
from repair_bike.models import Repair_Bike

# Create your views here.

def showRepairBike(request,modify_res=None):
    return render(request, 'repair_bike/add_repair_bike.html', {'res':modify_res})

def addRepairBike(request):
    repair_bike_id = request.POST.get('repair_bike_id')
    repair_bike_customer_id = request.POST.get('repair_bike_customer_id')
    repair_bike_number = request.POST.get('repair_bike_number')
    repair_bike_bill = request.POST.get('repair_bike_bill')
    repair_bike_type = request.POST.get('repair_bike_type')
    repair_bike_description = request.POST.get('repair_bike_description')
    add_repair_bike = Repair_Bike(repair_bike_id=repair_bike_id,repair_bike_customer_id=repair_bike_customer_id,
                              repair_bike_number=repair_bike_number,repair_bike_bill=repair_bike_bill,
                              repair_bike_type=repair_bike_type,repair_bike_description=repair_bike_description)
    add_repair_bike.save()
    return showRepairBike(request)

def showEditRepairBike(request,msg=None):
    rec = Repair_Bike.objects.all()
    return render(request, 'repair_bike/edit_repair_bike.html', {'my_rec':rec, 'msg':msg})

def editRepairBike(request,msg=None):
    repair_bike_id = request.POST.get('repair_bike_id')
    update_data = Repair_Bike.objects.filter(repair_bike_id = repair_bike_id)
    res = list(update_data)[0]
    return showRepairBike(request,modify_res=res)

def deleteRepairBike(request):
    repair_bike_id = request.POST.get('repair_bike_id')
    Repair_Bike.objects.filter(repair_bike_id = repair_bike_id).delete()
    return showEditRepairBike(request, msg='Delete Repair Bike Successfully')

def searchRepairBike(request):
    repair_bike_id = request.POST.get('repair_bike_id')
    search_data = Repair_Bike.objects.filter(repair_bike_id=repair_bike_id)
    res = list(search_data)[0]
    return show_searchRepairBike(request,modify_res=res)

def show_searchRepairBike(request,modify_res=None):
    return render(request, 'repair_bike/search_repair_bike.html', {'res':modify_res})