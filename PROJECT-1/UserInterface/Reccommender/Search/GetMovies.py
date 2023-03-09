
import pandas as pd


MOVIE_DATA=pd.read_csv('static/DATASETS/movies.csv')

class AMovie():
    def __init__(self,id):
        try:
            # MOVIE_DATA=None
            df=MOVIE_DATA[MOVIE_DATA['id']==id]
            print(type(df))
            # print(df)
        except:
            print('Wrong id')
        try:
            self.name=df.loc[0,'title']
            print(self.name)
            self.link=df.loc[0,'homepage']
            self.releaseDate=df.loc[0,'release_date']
            self.runtime=df.loc[0,'runtime']
            self.tagline=df.loc[0,'tagline']
            self.vote=df.loc[0,'vote_average']
        except:
            print("Error at AMovie ")
        
    


class GetMovies():

    """Gets list of movie ids and return list of movie objects"""
    # def getMovie(self):

    #     m1={'name':'Avatar','Actor':'simeone','director':'james'}
    #     m2={'name':'SUperman','Actor':'simeone','director':'james'}
    #     m3={'name':'ironman','Actor':'simeone','director':'james'}
    #     m4={'name':'Thor','Actor':'simeone','director':'james'}
    #     m5={'name':'Love today','Actor':'simeone','director':'james'}

    #     context=[m1,m2,m3,m4,m5]

    #     return context
    def getMovieObjs(self,movie_ids):
        movie_obj_list=[]
        for id in movie_ids:
            mv=AMovie(id=id)
            movie_obj_list.append(mv)

        return movie_obj_list
        

