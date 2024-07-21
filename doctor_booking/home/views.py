from django.shortcuts import render
from .models import departments,doctors
from .forms import booking_form

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form=booking_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = booking_form
    dict_form ={
        'form': form
    }
    return render(request,'booking.html',dict_form)

def Doctors(request):
    doc={
        'doc': doctors.objects.all()
    }
    return render(request,'doctors.html',doc)

def contact(request):
    return render(request,'contact.html')

def department(request):
    context={
        'dpt':departments.objects.all()}
    return render(request,'department.html',context)