from django.shortcuts import render,redirect
from .forms import AdminSignUpForm, CustomerSignUpForm
from django.contrib.auth import login,authenticate
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'admin'
            user.save()
            login(request, user)
            return redirect('admin_login')  
    else:
        form = AdminSignUpForm()
    return render(request, 'menu/signup_admin.html', {'form': form})

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'customer'
            user.save()
            login(request, user)
            return redirect('customer_dashboard')  # Change to appropriate URL
    else:
        form = CustomerSignUpForm()
    return render(request, 'menu/signup_customer.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.user_type == 'admin':
            login(request, user)
            return redirect('admin_dashboard')  # Change to appropriate URL
        else:
            # Handle invalid login
            return render(request, 'menu/admin/login_admin.html', {'error': 'Invalid login credentials'})
    return render(request, 'menu/login_admin.html')

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.user_type == 'customer':
            login(request, user)
            return redirect('customer_dashboard')  # Change to appropriate URL
        else:
            # Handle invalid login
            return render(request, 'menu/customer/login_customer.html', {'error': 'Invalid login credentials'})
    return render(request, 'menu/login_customer.html')