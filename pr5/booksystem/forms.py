from django import forms
from django.contrib.auth.models import User
from .models import Flight, Document


class PassengerInfoForm(forms.Form):
    leave_city = forms.CharField(label='leave_city', max_length=100)
    arrive_city = forms.CharField(label='arrive_city', max_length=100)
    leave_date = forms.DateField(label='leave_date')


# 自定义Flight对象的输入信息
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ['user']  # user信息不能从后台输入


# 用户需要输入的字段
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DocumentForm(forms.ModelForm):
    c = (("A", "male"), ("B", "female"))
    username = forms.CharField(required=False)
    gender = forms.ChoiceField(required=False,choices=c,label="gender")
    email = forms.CharField(required=False)
    birthday = forms.DateField(label=('birthday'),widget=forms.DateInput(
            attrs={'placeholder': '____/__/__', 'class': 'date'}))
    country = forms.CharField(required=False)
    number = forms.CharField(required=False)

    class Meta:
        model = Document

        fields = [
            'username',
            'gender',
            'email',
            'birthday',
            'country',
            'number',
        ]
