from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

class loginUserForm(forms.Form):
    username=forms.CharField(max_length=30,min_length=4,label='نام کاربری')
    password=forms.CharField(min_length=8,label='پسورد',widget=forms.PasswordInput)

class addbaner(forms.ModelForm):
    class Meta:
        model=apps.get_model('participation','banernews')
        fields={'title','description','image'}
        labels={'title':'عنوان','description':'متن خبر','image':'تصویر بنر اخبار ویژه'}
class news(forms.ModelForm):
    class Meta:
        model=apps.get_model('participation','news')
        fields=['day','month','year','description','image','title']        
        labels={'day':'روز','month':'ماه','year':'سال','description':'متن خبر','image':'تصویر خبر','title':'عنوان'}

class participate(forms.ModelForm):
    class Meta:
        model=apps.get_model('participation','participate')
        fields=['day','month','year','description','image','title']        
        labels={'day':'روز','month':'ماه','year':'سال','description':'متن خبر','image':'تصویر مشارکت','title':'عنوان'}

class volenteer(forms.ModelForm):
    class Meta:
        model=apps.get_model('participation','volenteer')
        fields=['fullname','career','tel','address']
        labels={'fullname':'نام و نام خانوادگی','career':'شغل','tel':'شماره تماس','address':'آدرس'}

class createUserCustomer(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        labels={'first_name':'نام','last_name':'نام خانوادگی','username':'نام کاربری','password':'پسورد'}
        widgets={
        'password': forms.PasswordInput()
        }

class messageadmin(forms.ModelForm):
    class Meta:
        model=apps.get_model('participation','message')
        fields=['msg']
        labels={'msg':'متن پیام'}