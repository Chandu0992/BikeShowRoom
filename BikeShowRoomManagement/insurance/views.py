from django.shortcuts import render
from insurance.models import Insurance

# Create your views here.

def showInsurance(request,modify_res=None):
    return render(request, 'insurance/add_insurance.html', {'res':modify_res})

def addInsurance(request):
    insurance_id = request.POST.get('insurance_id')
    insurance_bike_id = request.POST.get('insurance_bike_id')
    insurance_number = request.POST.get('insurance_number')
    insurance_date = request.POST.get('insurance_date')
    insurance_expiry = request.POST.get('insurance_expiry')
    insurance_amount = request.POST.get('insurance_amount')
    insurance_type = request.POST.get('insurance_type')
    insurance_description = request.POST.get('insurance_description')

    add_insurance = Insurance(insurance_id=insurance_id,insurance_bike_id=insurance_bike_id,insurance_number=insurance_number,
                              insurance_date=insurance_date,insurance_expiry=insurance_expiry,insurance_amount=insurance_amount,
                              insurance_type=insurance_type,insurance_description=insurance_description)
    add_insurance.save()
    return showInsurance(request)

# insurance_id,insurance_bike_id,insurance_number,insurance_date,
#     insurance_expiry,insurance_amount,insurance_type,insurance_description

def showEditInsurance(request,msg=None):
    rec = Insurance.objects.all()
    return render(request, 'insurance/edit_insurance.html', {'my_rec':rec, 'msg':msg})

def editInsurance(request,msg=None):
    insurance_id = request.POST.get('insurance_id')
    update_data = Insurance.objects.filter(insurance_id = insurance_id)
    res = list(update_data)[0]
    return showInsurance(request,modify_res=res)

def deleteInsurance(request):
    insurance_id = request.POST.get('insurance_id')
    Insurance.objects.filter(insurance_id = insurance_id).delete()
    return showEditInsurance(request, msg='Delete Insurance Successfully')

def searchInsurance(request):
    insurance_id = request.POST.get('insurance_id')
    search_data = Insurance.objects.filter(insurance_id=insurance_id)
    res = list(search_data)[0]
    return show_searchInsurance(request,modify_res=res)

def show_searchInsurance(request,modify_res=None):
    return render(request, 'insurance/search_insurance.html', {'res':modify_res})