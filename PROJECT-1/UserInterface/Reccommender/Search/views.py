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