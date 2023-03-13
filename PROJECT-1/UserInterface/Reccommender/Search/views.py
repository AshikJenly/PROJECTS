from django.shortcuts import render,redirect

from .GetMovies import GetMovies,GetFirst
from .reccommender import Reccomender
from .CorrectMovieName import MovieName
GF=GetFirst()
GT=GetMovies()
REC_MOV=Reccomender()
CorrectMovie_Name=MovieName()
# Create your views here.
def Movie_Page_view(request):
    try:
        if request.session.get('isLogin')==True:
            print('request.session.get(\'isLogin\') :',request.session.get('isLogin'))
            if request.method =='POST':
                val=request.POST.get('movie')
                movie_name=CorrectMovie_Name.get_appropriate_name(val)
                #get movie ids
                ids=REC_MOV.GetTopMoviesId(movie_name)
                
                movies=GT.getMovieObjs(ids)
                context={'movies':movies,'ishome':False}
                return render(request,"Movies/movies.html",context)
            else:
                ids=GF.getTop15Ids()
                movies=GT.getMovieObjs(ids)
                context={'movies':movies,'ishome':True}
                return render(request,"Movies/movies.html",context)
        else:
            
            return redirect('http://127.0.0.1:8000/')
            # return render(request,'front/home.html',{'log':True,'reg':False,'otp':False,'Message':"You have to login first!"})#after database code ,render movie page
    except:
            return render(request,'front/home.html',{'log':True,'reg':False,'otp':False,'Message':"You have to login first!"})#after database code ,render movie page
