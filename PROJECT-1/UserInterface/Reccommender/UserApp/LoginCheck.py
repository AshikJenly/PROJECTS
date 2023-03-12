from .models import UserInfoDB1


def checkLogin(email,password):
    objs=UserInfoDB1.objects.all()
    for obj in objs:
        if obj.email==email:
            if obj.password==password:
                return None,True
            else:
                return "Wrong Password ,Please try again!",False
        
    return "Sorry,User does'nt exist please register.",False    
    
def checkRegister(email):
    objs=UserInfoDB1.objects.all()
    for obj in objs:
        if obj.email==email:
            return True
        
    return False    
    