from .models import UserInfoDB


def checkLogin(email,password):
    objs=UserInfoDB.objects.all()
    for obj in objs:
        print(obj.fname)