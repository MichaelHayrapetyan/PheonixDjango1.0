from .models import Car
from .forms import RegistrationForm, LoginForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CommentForm


def home_page(request):
    return render(request, 'home/home_page.html')


def supercars(request):
    cars = Car.objects.all()
    return render(request, 'models/supercars.html', {'cars': cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'models/detail.html', {'car': car})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'login/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def exclusive(request):
    cars = Car.objects.all()
    return render(request, 'models/exclusive.html', {'cars': cars})



def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comments:all')
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})
