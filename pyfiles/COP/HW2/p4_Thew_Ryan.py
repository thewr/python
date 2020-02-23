import csv

def read_csv(filename):
    obj_read = open(filename,'r', encoding = 'utf-8')
    with obj_read:
        reader = csv.reader(obj_read)
        movie = dict()
        movie_list = []
        for line in reader:
            movie = {
                'Title': line[0],
                'Year': line[1],
                'Director': line[2],
                'Actor': line[3]
            }
            movie_list.append(movie)


        combo = []

        films = []
        for movie in movie_list:
            combo.append((movie['Director'], movie['Actor']))
            films.append((movie['Title'], movie['Director'], movie['Actor']))



        set_combo = set(combo)
        set_films = set(films)


        top = []
        top_combo = {}
        for combo in set_combo:
            count = 0
            for film in set_films:
                if (set(combo) <= set(film)):
                    count += 1
                    top_combo = {
                        'Title': film[0],
                        'Director': film[1],
                        'Actor': film[2],
                        'Count': count
                    }

                    top.append(top_combo)

        for t in top:
            if t['Count'] > 3:
                print(t)


def display_top_collaborations():
    read_csv('imdb-top-casts.csv')

display_top_collaborations()
