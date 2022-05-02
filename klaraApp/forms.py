from django import forms
from django.contrib.auth.models import User

from klaraApp.models import ClientProfile, Appointment


class ProfileUserForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={"placeholder": "Имя","required class":"general_inputs reg_inputs"}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={"placeholder": "Фамилия","required class":"general_inputs reg_inputs"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder": "Почта","required class":"general_inputs reg_inputs"}))
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"placeholder": "Логин","required class":"general_inputs reg_inputs"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": "Пароль","required class":"general_inputs reg_inputs"}))

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]

class ProfielExtrForm(forms.ModelForm):

    photo = forms.ImageField(label="Фото",widget=forms.FileInput(attrs={"required class":"general_inputs reg_inputs","placeholder":"Фото"}))


    class Meta:
        model = ClientProfile
        fields = ["photo"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"required class":"general_inputs reg_inputs","placeholder":"Логин"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"required class":"general_inputs reg_inputs","placeholder":"Пароль"}))


TIMESLOT_LIST = (
    (0, '09:00 – 10:30'),
    (1, '11:00 – 12:30'),
    (2, '13:00 – 14:30'),
    (3, '15:00 – 16:30'),
    (4, '17:00 – 18:30'),
    (5, '19:00 – 20:30'))

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    timeslot = forms.ChoiceField(choices=TIMESLOT_LIST, widget=forms.RadioSelect())
    class Meta:
        model = Appointment
        fields = ["service","date","timeslot",]