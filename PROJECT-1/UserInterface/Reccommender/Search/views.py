from django.shortcuts import render,redirect

from .GetMovies import GetMovies
from .reccommender import Reccomender
GT=GetMovies()
REC_MOV=Reccomender()

# Create your views here.
def Movie_Page_view(request):
    if request.method =='POST':
        val=request.POST.get('movie')

        #get movie ids
        ids=REC_MOV.GetTopMoviesId(19995)
        movies=GT.getMovieObjs(ids)

        context={'movies':movies}
        return render(request,"Movies/movies.html",context)
    else:

        return render(request,"Movies/movies.html",{})