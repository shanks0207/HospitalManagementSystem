from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddPatientForm
from .models import Patient
from user.models import Staff
# from user.views import *

# Create your views here.

def patient(request):
    records = Staff.objects.all()
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In !")
            return redirect('patients')
        else:
            messages.success(request, "There was An Error Logging In, Please try Again.....")
            return redirect('home')
    else:
        return render(request, 'patients.html', {'patient_record': patient_record})

# def logout_user(request):
#     logout(request)
#     messages.success(request, "You Hasvebeen Logged Out...")
#     return redirect('home')

# def register_user(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #Authenticate and login
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, "You Have Successfully Resistered ! WELCOME !")
#             return redirect('home')
#     else:
#         form = SignUpForm()
#         return render(request, 'register.html', {'form':form})
#     return render(request, 'register.html', {'form':form})


def patient_record(request, pk):
    if request.user.is_authenticated:
        #Look up Records
        staff_record = Patient.objects.get(id=pk)
        return render(request, 'patient_record.html', {'patient_record':patient_record})
    else:
        messages.success(request, "You Must Be Logged In To View Requested Data")
        return redirect('home')


def delete_patient(request, pk):
    if request.user.is_authenticated:
        delete_it = Patient.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Records Deleted Successfully....")
        return redirect('patient')
    else:
        messages.success(request, "you Must Be Logged In To Delete This Data." )
        return redirect('home')


def add_patient(request):
    form = AddPatientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added ")
                return redirect('patient')
        return render(request, 'add_patient.html', {'form':form})
    else:
        messages.success(request, "You Must Be LoggedIn .....")
        return redirect('home')
    
def update_patient(request, pk):
    if request.user.is_authenticated:
        current_record = Patient.objects.get(id=pk)
        form = AddPatientForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated. !")
            return redirect('patient')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In..")
        return redirect('home')
        
def patient_list(request):
    records = Patient.objects.all()

    # Filtering
    gender_filter = request.GET.get('gender')
    if gender_filter:
        records = records.filter(gender=gender_filter)

    sector_filter = request.GET.get('sector')
    if sector_filter:
        records = records.filter(sector=sector_filter)

    # Sorting
    sort_by = request.GET.get('sort')
    if sort_by:
        records = records.order_by(sort_by)

    context = {
        'records': records
    }
    return render(request, 'patient_record.html', context)