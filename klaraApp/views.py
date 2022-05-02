from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group

from django.shortcuts import render, redirect

from klaraApp.forms import ProfileUserForm, ProfielExtrForm, LoginForm, EventForm
from .models import Appointment, ClientProfile


def is_profile(user):
    return user.groups.filter(name='CLIENT').exists()

def afterlogin_view(request):
    if is_profile(request.user):
        accountapproval=ClientProfile.objects.all().filter(user_id=request.user.id)
        if accountapproval:
            return redirect('profile')


def index(request):
    return render(request, 'klaraApp/index.html', {'title': 'главная'})

def about(request):
    return render(request, 'klaraApp/about.html', {'title': 'о нас'})

def booking(request):
    return render(request, 'klaraApp/booking.html', {'title': 'запись'})

def contacts(request):
    return render(request, 'klaraApp/contacts.html', {'title': 'контакты'})

def registration(request):
    form = ProfileUserForm()
    form2 = ProfielExtrForm()
    if request.method == "POST":
        form = ProfileUserForm(request.POST)
        form2 = ProfielExtrForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            user2 = form2.save(commit=False)
            user2.user = user
            user2.save()
            my_profile_group = Group.objects.get_or_create(name="CLIENT")
            my_profile_group[0].user_set.add(user)
            return redirect("login")

    context = {
        "form":form,
        "form2":form2,
    }
    return render(request, "klaraApp/registrations.html", context)


def login_user(request):
    form3 = LoginForm()
    if request.method == "POST":
        form3 = LoginForm(request.POST)
        if form3.is_valid():
            user3 = authenticate(username=form3.cleaned_data['username'], password=form3.cleaned_data['password'])
            if user3 is not None:
                login(request, user3)
                return redirect("after_login")

    context = {
        "form3":form3
    }
    return render(request, 'klaraApp/login.html', context)

@user_passes_test(is_profile)
def my_profile(request):
    events = Appointment.objects.filter(client_id=request.user.id)
    count_events = Appointment.objects.filter(client_id=request.user.id).count()

    users = ClientProfile.objects.get(user_id=request.user.id)
    context = {
    "users":users,
    "events":events,
    "count_events":count_events,
    }
    return render(request, 'klaraApp/profile.html', context)

@user_passes_test(is_profile)
def add_event(request):
    events = Appointment.objects.all()
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.client = request.user
            f.save()
            return redirect("profile")


    context = {
        "form":form,
        "events":events,
    }
    return render(request,"klaraApp/booking.html",context)
