from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
from . models import ImgModel
# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignupForm()
    return render(request,'signup.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            img = form.cleaned_data.get('profile_pic')
            obj = ImgModel.objects.create(img = img)
            user = authenticate(username=username, password=password)
            obj.save()
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def patient(request):
    return render(request,'patient.html')


def doctor(request):
    return render(request,'doctor.html')
