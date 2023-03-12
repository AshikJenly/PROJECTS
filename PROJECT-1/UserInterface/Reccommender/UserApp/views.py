from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .user_info import UserInfo
from .verify_email import MailVerify
from . import writeintoDb
from .LoginCheck import checkLogin,checkRegister


mail_check=MailVerify()
uf=UserInfo()

# Create your views here.
def home_page_view(requests):
    if requests.method=="POST":
        email=requests.POST.get('email')
        password=requests.POST.get('pass')
        Message,IsValid=checkLogin(email=email,password=password)

        if IsValid:
            return HttpResponseRedirect('http://127.0.0.1:8000/movies')#after database code ,render movie page
        else:
            return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False,'Message':Message})#after database code ,render movie page

    else:
        data = requests.GET.get('data')
        if data!=None:
            return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False,'Message':data})
        else:
            return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False,'Message':""})



def Register_page_view(requests):
    if requests.method=="GET":

        return render(requests,'front/home.html',{'log':False,'reg':True,'otp':False,'Message':""})
    
    elif requests.method=='POST':

        fname=requests.POST.get('fname')
        lname=requests.POST.get('lname')
        email=requests.POST.get('email')
        college=requests.POST.get('cname')
        password=requests.POST.get('u_pass')

        # Check existing email
        isExist=checkRegister(email=email)
        if isExist:

            return render(requests,'front/home.html',{'log':False,'reg':True,'otp':False,"Message":"Mail id has been registered already!"})
        else:
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
                return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/')
                # return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False})
            else :
                url = 'http://127.0.0.1:8000/' + '?data=' + "Wrong OTP ,Please Try again!"
                return HttpResponseRedirect(redirect_to=url)

                # return render(requests,'front/home.html',{'log':True,'reg':False,'otp':False,"Message":"Wrong OTP ,Please Try again!"})
            
        except:
            print("Error occured in redirecting")
            url ='http://127.0.0.1:8000/' + '?data=' + ""
            return HttpResponseRedirect(redirect_to=url)
