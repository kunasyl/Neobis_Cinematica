from showtimes import models as showtime_models
from movies import models as movie_models


class MovieRepos:
    showtime_model = showtime_models.Showtime
    movie_models = movie_models.Movie

    def get_movie_showtimes(self, movie_id):
        return self.showtime_model.objects.filter(movie_id=movie_id)

    def get_movies(self, ):
        return self.movie_models.objects.all()
