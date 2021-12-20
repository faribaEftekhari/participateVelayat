from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

# Create your models here.

class samans(models.Model):
    title=models.CharField(max_length=200)
    link=models.CharField(max_length=200)
    
class banernews(models.Model):
    image=models.ImageField(default='1.jpg',upload_to='ImageSlider/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=300,default=' ')
    description=models.TextField(default=' ',blank=True)

DAY_CHOICES=[(str(x),str(x)) for x in range(1, 32)]
MONTH_CHOICE=(
('مهر','مهر'),
('آبان','آبان'),
('آذر','آذر'),
('دی','دی'),
('بهمن','بهمن'),
('اسفند','اسفند'),
('فروردین','فروردین'),
('اردیبهشت','اردیبهشت'),
('خرداد','خرداد'),
('تیر','تیر'),
('مرداد','مرداد'),
('شهریور','شهریور'),

)
YEAR_CHOICES=[(str(x),str(x)) for x in range(1400,1405)]

class news(models.Model):    
    title=models.CharField(max_length=300)
    day=models.CharField(max_length=6, choices=DAY_CHOICES, default='1')
    month=models.CharField(max_length=15,choices=MONTH_CHOICE,default='mehr')
    year=models.CharField(max_length=6, choices=YEAR_CHOICES, default='1400')
    description=models.TextField(default=' ',blank=True)
    image=models.ImageField(default='2.jpg',upload_to='news/',null=True,blank=True)

    def snippet(self):
        return self.description[:35]+ '  ...'

class participate(models.Model):    
    title=models.CharField(max_length=300)
    day=models.CharField(max_length=6, choices=DAY_CHOICES, default='1')
    month=models.CharField(max_length=15,choices=MONTH_CHOICE,default='mehr')
    year=models.CharField(max_length=6, choices=YEAR_CHOICES, default='1400')
    description=models.TextField(default=' ',blank=True)
    image=models.ImageField(default='3.jpg',upload_to='participate/',null=True,blank=True)
    

    def snippet(self):
        return self.description[:15]+ '  ...'
    def titlesnippet(self):
         return self.title[:30]+ '  ...'

class volenteer(models.Model):
    fullname=models.CharField(max_length=150)    
    career=models.CharField(max_length=300)
    tel=models.CharField(max_length=11)
    address=models.TextField(default=' ',blank=True)
    # email=models.EmailField(validators=[EmailValidator(message="لطفا ایمیل خود را به درستی وارد کنید")],blank=True,unique=True)
    

class message(models.Model):
    msg=models.TextField(default=' ',blank=True)