from . import repos


class MovieServices:
    movie_repos = repos.MovieRepos()

    def get_movie_showtimes(self, movie_id):
        return self.movie_repos.get_movie_showtimes(movie_id=movie_id)

    def get_movies(self):
        return self.movie_repos.get_movies()

    def get_soon_movies(self, max_days=30):
        """
        Returns movies that will be soon (premiere) in a month by default.
        """
        return self.movie_repos.get_soon_movies(max_days=max_days)
