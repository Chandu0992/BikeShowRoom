from django.shortcuts import render
from customer.models import Customer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def showCustomer(request,modify_res=None):
    return render(request, 'customer/add_customer.html', {'res':modify_res})

def addCustomer(request):
    customer_id = request.POST.get('customer_id')
    customer_name = request.POST.get('customer_name')
    customer_mobile = request.POST.get('customer_mobile')
    customer_email = request.POST.get('customer_email')
    customer_username = request.POST.get('customer_username')
    customer_password = request.POST.get('customer_password')
    customer_address = request.POST.get('customer_address')
    customer_pwd_hash = make_password(customer_password)
    add_customer = Customer(customer_id=customer_id,customer_name=customer_name,customer_mobile=customer_mobile,
                            customer_email=customer_email,customer_username=customer_username,customer_password=customer_pwd_hash,
                            customer_address=customer_address)
    add_customer.save()
    return showCustomer(request)

def showEditCustomer(request,msg=None):
    rec = Customer.objects.all()
    return render(request, 'customer/edit_customer.html', {'my_rec':rec, 'msg':msg})

def editCustomer(request,msg=None):
    customer_id = request.POST.get('customer_id')
    update_data = Customer.objects.filter(customer_id = customer_id)
    res = list(update_data)[0]
    return showCustomer(request,modify_res=res)

def deleteCustomer(request):
    customer_id = request.POST.get('customer_id')
    Customer.objects.filter(customer_id = customer_id).delete()
    return showEditCustomer(request, msg='Delete Repair Bike Successfully')

def searchCustomer(request):
    customer_id = request.POST.get('customer_id')
    search_data = Customer.objects.filter(customer_id=customer_id)
    res = list(search_data)[0]
    return show_searchCustomer(request,modify_res=res)

def show_searchCustomer(request,modify_res=None):
    return render(request, 'customer/search_customer.html', {'res':modify_res})