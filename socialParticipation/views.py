from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.apps import apps
from . import forms
from django.contrib.auth.models import User
from django.db.models import Q

def index(request):
    form=forms.loginUserForm()    
    return render(request,'index.html',{'form':form})
def home(request):
    samans=fetchSaman_view()
    fiveBaner=fivebaner_view()
    news=fetchnews_view()
    participate=fetchparticipate_view()
    return render(request,'home.html',{'samans':samans,'fiveBaner':fiveBaner,'news':news,'participate':participate})
def about(request):
    samans=fetchSaman_view()    
    news=fetchnews_view()
    return render(request,'about.html',{'samans':samans,'news':news})

def afterlogin_view(request):    
    username = request.POST.get("username",'')
    password = request.POST.get("password",'')    
    user = authenticate(username=username, password=password)    
    if user is not None:
        login(request, user)
        return render(request,'adminhome.html')
    return redirect('')
   
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('')
    return redirect('adminhome')

#جستجو
def search_view(request):    
    qry=request.GET['qry']    
    participate=apps.get_model('participation','participate').objects.filter(Q(title__icontains = qry)|Q(description__icontains = qry)).order_by('-id')
    samans=fetchSaman_view()
    fiveBaner=fivebaner_view()
    news=fetchnews_view()    
    return render(request,'home.html',{'samans':samans,'fiveBaner':fiveBaner,'news':news,'participate':participate})
#register samans and show them
@login_required(login_url='home')
def registerSaman_view(request):    
    title=request.GET.get('title1')
    link=request.GET.get('link')
    if title is not None and link is not None:
        saman1=apps.get_model('participation','samans').objects.create()
        saman1.title=title
        saman1.link=link
        saman1.save()
    samans=apps.get_model('participation','samans').objects.all().order_by('-id')
    return render(request,'samans.html',{'samans':samans})

def fetchSaman_view():
    samans=apps.get_model('participation','samans').objects.order_by('-id')[:8]
    return samans
#واکشی اخبارها برای صفحه خانگی
def fetchnews_view():
    news=apps.get_model('participation','news').objects.order_by('-id')[:8]
    return news
#واکشی فعالیت های مشارکتی
def fetchparticipate_view():
    participate=apps.get_model('participation','participate').objects.order_by('-id')[:6]
    return participate
#ثبت عکس بنر ویژه خبری
@login_required(login_url='home')
def addbaner_view(request):
    if request.POST:
        form=forms.addbaner(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save()
            instance.save()
            return render(request,'successfully.html')
    else:
        form=forms.addbaner()
    baners=apps.get_model('participation','banernews').objects.all().order_by('-id')
    return render(request,'banernews.html',{'form':form,'baners':baners})
#fetch five banernews for home
def fivebaner_view():
    fiveBaner=apps.get_model('participation','banernews').objects.order_by('-id')[:5]
    return fiveBaner
#افزودن خبر 
@login_required(login_url='home')
def addnews_views(request):
    if request.POST:
        form=forms.news(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save()
            instance.save()
            return render(request,'successfully.html')
    else:
        form=forms.news()
    news=apps.get_model('participation','news').objects.all().order_by('-id')
    return render(request,'addnews.html',{'form':form,'news':news})
#نمایش جزئیات خبر
def newsdetail_view(request,pk):
    newsdetail=apps.get_model('participation','news').objects.get(id=pk)
    samans=fetchSaman_view()    
    news=fetchnews_view()
    return render(request,'newsdetail.html',{'newsdetail':newsdetail,'samans':samans,'news':news})
#ثبت فعالیت های مشارکتی
@login_required(login_url='home')
def addparticipate_view(request):
    if request.POST:
        form=forms.participate(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save()
            instance.save()
            return render(request,'successfully.html')
    else:
        form=forms.participate()
    parts=apps.get_model('participation','participate').objects.all().order_by('-id')
    return render(request,'participate.html',{'form':form,'parts':parts}) 
#ثبت داوطلب
def addvolenteer_view(request):
    if request.POST:        
        form=forms.volenteer(request.POST)
        if form.is_valid():
            instance=form.save()
            instance.save()
            return render(request,'successfully.html')
        else:
            return render(request,'notvalid.html')
    else:
        form=forms.volenteer()
    return render(request,'registerVolenteer.html',{'form':form}) 

#لیست داوطلبان
@login_required(login_url='index')
def showvolenteer_view(request):
    volenteers=apps.get_model('participation','volenteer').objects.all().order_by('-id')
    return render(request,'volenteers.html',{'volenteers':volenteers})

#حذف داوطلب
@login_required(login_url='home')
def deletevolenteer_view(request,pk):
    volenteer=apps.get_model('participation','volenteer').objects.get(id=pk)
    volenteer.delete()
    volenteers=apps.get_model('participation','volenteer').objects.all().order_by('-id')
    return render(request,'volenteers.html',{'volenteers':volenteers})

#حذف سمن
@login_required(login_url='home')
def deletesaman_view(request,pk):
    saman=apps.get_model('participation','samans').objects.get(id=pk)
    saman.delete()
    samans=apps.get_model('participation','samans').objects.all().order_by('-id')
    return render(request,'samans.html',{'samans':samans})

#ویرایش پروفایل
@login_required(login_url='home')
def editprofile_view(request):
    activeuser=User.objects.get(id=request.user.id)
    userForm=forms.createUserCustomer(instance=activeuser)
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.createUserCustomer(request.POST,instance=activeuser)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            return redirect('')
    return render(request,'profile.html',context=mydict)


#آرشیو سالیانه فعالیتهای مشارکتی
def archive_views(request,pk):    
    participate=apps.get_model('participation','participate').objects.filter(year=pk)
    samans=fetchSaman_view()
    fiveBaner=fivebaner_view()
    news=fetchnews_view()    
    return render(request,'archive.html',{'samans':samans,'fiveBaner':fiveBaner,'news':news,'participate':participate})

#نمایش جزئیات اخبار ویژه بنر
def specialnews_view(request,pk):
    newsdetail=apps.get_model('participation','banernews').objects.get(id=pk)
    samans=fetchSaman_view()    
    news=fetchnews_view()
    return render(request,'newsdetail.html',{'newsdetail':newsdetail,'samans':samans,'news':news})

#ثبت پیام مدیر
@login_required(login_url='home')
def messageadmin_view(request):
    if request.POST:
        form=forms.messageadmin(request.POST)
        if form.is_valid():            
            instance=form.save()
            instance.save()
            return render(request,'successfully.html')
    else:
        form=forms.messageadmin()
    return render(request,'registermessage.html',{'form':form}) 

#نمایش پیام مدیر
def showmessage_view(request):
    msgg=apps.get_model('participation','message').objects.order_by('-id')[:2]  
    samans=fetchSaman_view()    
    news=fetchnews_view()
    return render(request,'showmessage.html',{'msgg':msgg,'samans':samans,'news':news})

#حذف خبرها
@login_required(login_url='home')
def delnews_view(request,pk):
    new=apps.get_model('participation','news').objects.get(id=pk)
    new.delete()    
    news=apps.get_model('participation','news').objects.all().order_by('-id')
    form=forms.news()
    return render(request,'addnews.html',{'form':form,'news':news})

#حذف بنر
@login_required(login_url='home')
def delbaner_view(request,pk):
    baner=apps.get_model('participation','banernews').objects.get(id=pk)
    baner.delete()
    baners=apps.get_model('participation','banernews').objects.all().order_by('-id')
    form=forms.addbaner()
    return render(request,'banernews.html',{'form':form,'baners':baners})

#حذف مشارکت
@login_required(login_url='home')
def delparticipate_view(request,pk):
    part=apps.get_model('participation','participate').objects.get(id=pk)
    part.delete()
    parts=apps.get_model('participation','participate').objects.all().order_by('-id')
    form=forms.participate()
    return render(request,'participate.html',{'form':form,'parts':parts})

#جزئیات مشارکتها
def partnews_view(request,pk):
    partdetail=apps.get_model('participation','participate').objects.get(id=pk)
    samans=fetchSaman_view()    
    news=fetchnews_view()
    return render(request,'partdetail.html',{'partdetail':partdetail,'samans':samans,'news':news})