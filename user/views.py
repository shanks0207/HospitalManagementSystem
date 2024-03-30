from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Staff

# Create your views here.

def home(request):
    records = Staff.objects.all()
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In !")
            return redirect('home')
        else:
            messages.success(request, "There was An Error Logging In, Please try Again.....")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You Hasvebeen Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Resistered ! WELCOME !")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def Staff_record(request, pk):
    if request.user.is_authenticated:
        #Look up Records
        staff_record = Staff.objects.get(id=pk)
        return render(request, 'record.html', {'staff_record':staff_record})
    else:
        messages.success(request, "You Must Be Logged In To View Requested Data")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Staff.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Records Deleted Successfully....")
        return redirect('home')
    else:
        messages.success(request, "you Must Be Logged In To Delete This Data." )
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added ")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be LoggedIn .....")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Staff.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated. !")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In..")
        return redirect('home')
        
def record_list(request):
    records = Staff.objects.all()

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
    return render(request, 'record_list.html', context)

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        messages.success(request, "You Must Be Logged In..")
        return redirect('home')
