
from .models import UserInfoDB


def writeIntoDB(uf):
    print("----------DB WRITE-----------")

    fname=uf.fname
    lname=uf.lname
    email=uf.email
    college=uf.college
    password=uf.password
    user_info= UserInfoDB(fname=fname, lname=lname,email=email,college=college,password=password)
    user_info.save()
    print(uf.fname,uf.password,uf.email)
    print("----------DB WRITE-----------")

