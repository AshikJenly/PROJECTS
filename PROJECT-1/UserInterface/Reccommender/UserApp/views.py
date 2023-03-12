from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from .user_info import UserInfo
from .verify_email import MailVerify
mail_check=MailVerify()
uf=UserInfo()

# Create your views here.
def home_page_view(requests):
    if requests.method=="POST":
        p=requests.POST.get('pass')
        print(requests.POST.get('email'))
        print(p)
        if p == 'ashik':
            return HttpResponseRedirect('http://127.0.0.1:8000/movies')#after database code ,render movie page
        return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False})#after database code ,render movie page

    return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False})
def Register_page_view(requests):
    if requests.method=="GET":

        return render(requests,'front/home.html',{'log':False,'reg':True,'otp':False})
    
    elif requests.method=='POST':
        # print('action : ',requests.path)

        fname=requests.POST.get('fname')
        lname=requests.POST.get('lname')
        email=requests.POST.get('email')
        college=requests.POST.get('cname')
        print(fname,lname,email,college)

        uf.values(fname=fname,lname=lname,email=email,college=college)
        otp_gen=mail_check.verifyOtp(email=email,name=(fname+" "+lname))
        print(otp_gen)
        uf.set_otp(otp=otp_gen)

        return render(requests,'front/home.html',{'log':False,'reg':False,'otp':True,'email':email})
def Otpview(requests):
    if requests.method == 'POST':
        otp=requests.POST.get('otp_user')
        print(otp)
        if uf.check_otp(otp):
            print('Otp verified','write into data base')
        return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False})

