from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from .user_info import UserInfo
from .verify_email import MailVerify
from . import writeintoDb
from .LoginCheck import checkLogin

mail_check=MailVerify()
uf=UserInfo()

# Create your views here.
def home_page_view(requests):
    if requests.method=="POST":
        p=requests.POST.get('pass')
        print(requests.POST.get('email'))
        
        checkLogin("",password=p)
        if p == 'ashik':
            return HttpResponseRedirect('http://127.0.0.1:8000/movies')#after database code ,render movie page
        return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False})#after database code ,render movie page

    return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False})
def Register_page_view(requests):
    if requests.method=="GET":

        return render(requests,'front/home.html',{'log':False,'reg':True,'otp':False,'wrong_otp':False})
    
    elif requests.method=='POST':
        # print('action : ',requests.path)

        fname=requests.POST.get('fname')
        lname=requests.POST.get('lname')
        email=requests.POST.get('email')
        college=requests.POST.get('cname')
        password=requests.POST.get('u_pass')
        # print(fname,lname,email,college,password)
        uf.values(fname=fname,lname=lname,email=email,college=college,password=password)
        otp_gen=mail_check.verifyOtp(email=email,name=(fname+" "+lname))
        print(otp_gen)
        uf.set_otp(otp=otp_gen)

        return render(requests,'front/home.html',{'log':False,'reg':False,'otp':True,'email':email})
def Otpview(requests):
    if requests.method == 'POST':
        try:
            otp=requests.POST.get('otp_user')
            print(otp)
            if uf.check_otp(otp):
                print('Otp verified')
                writeintoDb.writeIntoDB(uf)

                return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False})
            else :
                return HttpResponseRedirect('http://127.0.0.1:8000/Register')#after database code ,render movie page
            
        except:
             return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False})#after database code ,render movie page

