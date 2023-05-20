from . import repos


class MovieServices:
    movie_repos = repos.MovieRepos()

    def get_movie_showtimes(self, movie_id):
        return self.movie_repos.get_movie_showtimes(movie_id=movie_id)

    def get_movies(self):
        return self.movie_repos.get_movies()
