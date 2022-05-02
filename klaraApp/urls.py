from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('about', about, name = 'about'),
    # path('booking', booking, name = 'booking'),
    path('contacts', contacts, name = 'contacts'),
    path('registration', registration, name = 'registration'),
    path('login_user',login_user,name='login'),
    path('my_profile',my_profile,name='profile'),
    path("exit/", LogoutView.as_view(), name="exit"),
    path("after_login",afterlogin_view,name="after_login"),
    path("add_event",add_event,name='booking'),
]
