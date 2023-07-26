from django.shortcuts import render, redirect

# manual imports
from .models import Departments, Doctors, Booking
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

# home page
def index(request):
    return render(request, 'index.html')

# about section 
@login_required(login_url='/signin/')
def about(request):
    return render(request, 'about.html')

# appointment booking
@login_required(login_url='/signin/') 
def booking(request):
    doctorobj = Doctors.objects.all()
    context = { 'doctorobj' : doctorobj }

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        doctor_id = request.POST.get('doctor')
        doctor = Doctors.objects.get(pk=doctor_id)
        date = request.POST.get('date')

        # saving to database
        user = Booking(pat_name=name,pat_age=age,pat_phone=phone,pat_email=email,doc_name=doctor,book_date=date)
        user.save()
        messages.success(request, 'Appointment booking successful')
        return redirect('/')

    return render(request, 'booking.html', context)

# doctors list fetched from DB
@login_required(login_url='/signin/')
def doctors(request):
    dict_docs = {
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

# department list fetched from DB
@login_required(login_url='/signin/')
def department(request):
    dict_dept = {
        'dept' : Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)

# contact us page
@login_required(login_url='/signin/')
def contact(request):
   return render(request, 'contact.html')

# user registering
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        # checking credentials
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('signup')
            # user saving to DB
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                messages.success(request, 'Welcome, Sign Up successful')
                return redirect('home')
        else:
            messages.info(request, 'Password Mismatched')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

# user login
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        # checking credentials
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome Back, Sign In successful')
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

 # user logout
def logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully logouted')
    return redirect('/')