from django.shortcuts import render,redirect

from .GetMovies import GetMovies
from .reccommender import Reccomender
from .CorrectMovieName import MovieName
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
        print(ids)
        movies=GT.getMovieObjs(ids)
        # for movie in movies:
        #     # print(type(movie))
        #     # print(movie.name,movie.link)
        #     print('------------------')
        context={'movies':movies}
        return render(request,"Movies/movies.html",context)
    else:

        return render(request,"Movies/movies.html",{})