from django.shortcuts import render
from bike.models import Bike

# Create your views here.
def show_Home(request):
    return render(request,'Home_Page.html')

def showBike(request,modify_res=None):
    return render(request, 'bike/add_bike.html', {'res':modify_res})

def addBike(request):
    bike_id = request.POST.get('bike_id')
    bike_customer = request.POST.get('bike_customer')
    bike_number = request.POST.get('bike_number')
    bike_company = request.POST.get('bike_company')
    bike_type = request.POST.get('bike_type')
    bike_desc = request.POST.get('bike_desc')
    #bike_id,bike_customer,bike_number,bike_type,bike_description
    add_bike = Bike(bike_id=bike_id,bike_company=bike_company,bike_customer=bike_customer,bike_number=bike_number,bike_type=bike_type,bike_description=bike_desc)
    add_bike.save()
    return showBike(request)

def showEditBike(request,msg=None):
    rec = Bike.objects.all()
    return render(request, 'bike/edit_bike.html', {'my_rec':rec, 'msg':msg})

def editBike(request,msg=None):
    bike_id = request.POST.get('bike_id')
    print("Bike Id : ",bike_id)
    update_data = Bike.objects.filter(bike_id = bike_id)
    res = list(update_data)[0]
    return showBike(request,modify_res=res)

def deleteBike(request):
    id = request.POST.get('bike_id')
    Bike.objects.filter(bike_id = id).delete()
    return showEditBike(request, msg='Delete Bike Successfully')

def searchBike(request):
    pid = request.POST.get('bike_id')
    search_data = Bike.objects.filter(bike_id=pid)
    res = list(search_data)[0]
    return show_searchBike(request,modify_res=res)

def show_searchBike(request,modify_res=None):
    return render(request, 'bike/search_bike.html', {'res':modify_res})