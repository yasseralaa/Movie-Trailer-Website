import media
import fresh_tomatoes
import json
import urllib2


# main function
def main():
    # the movie db api
    moviedbapi = "http://api.themoviedb.org/3/discover/mo" \
                 "vie?api_key=fa4170617ad1260b3b65c4c0dc9997ef"
    # using urllib to load api content and json.load
    # method to extract it's json data
    moviedbdata = json.load(urllib2.urlopen(moviedbapi))
    # list to add movie objects
    movies = []
    # iterate throw json array of objects and extract data values with keys
    for movie in moviedbdata['results']:
        movie_object = media.Movie(
            movie['title'],
            "http://image.tmdb.org/t/p/w185/" + str(movie['poster_path']),
            get_trailer(movie['id']),
            movie['vote_average'])
        movies.append(movie_object)

    # calling the "open_movies_page" func from "fresh_tomatoes" module
    fresh_tomatoes.open_movies_page(movies)


# consuming trailer api with movie id
def get_trailer(movie_id):
    movietrailersapi = "http://api.themoviedb.org/3/movie/" + str(
        movie_id) + "/videos?api_key=fa4170617ad1260b3b65c4c0dc9997ef"
    moviedata = json.load(urllib2.urlopen(movietrailersapi))
    return "https://www.youtube.com/watch?v=" + moviedata['results'][0]['key']


# ensure that main func executing first
if __name__ == '__main__':
    main()
