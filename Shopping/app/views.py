from django.shortcuts import render

# Create your views here.
def ShowIndex(request):
    return render(request,'app/index.html')