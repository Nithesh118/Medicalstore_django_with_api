from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test

from .models import Medicine
from .forms import MedicineForm


def home(request):
    return render(request,'base.html')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import Customer

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                if Customer.objects.filter(username=username).exists():
                    error_message = "Username is already taken."
                    return render(request, 'signup.html', {'form': form, 'error_message': error_message})
                else:
                    user = User(username=username, password=password)
                    user.set_password(password)
                    user.save()
                    return redirect('login') 
            else:
                error_message = "Passwords do not match."
                return render(request, 'signup.html', {'form': form, 'error_message': error_message})
    else:
        form = SignupForm()
    return render(request, 'signup.html',{'form':form})


from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('list_medicines')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)

@login_required(login_url="/login/")
def list_medicines(request):
    medicines = Medicine.objects.all()
    return render(request, 'list_medicines.html', {'medicines': medicines})
@login_required(login_url='/login/')
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            return redirect('list_medicines')
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})
@login_required(login_url='/login/')
def edit_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            return redirect('list_medicines')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'edit_medicine.html', {'form': form})
@login_required(login_url='/login/')
def delete_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    medicine.delete()
    return redirect('list_medicines')
@login_required(login_url='/login/')

def search_medicine(request):
    query = request.GET.get('query')
    if query:
        medicines = Medicine.objects.filter(name__startswith=query)
    else:
        medicines = Medicine.objects.none()
    return render(request, 'search_medicine.html', {'medicines': medicines})










