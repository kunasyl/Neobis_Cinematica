from showtimes import models as showtime_models
from movies import models as movie_models

import datetime
import pytz


class MovieRepos:
    showtime_model = showtime_models.Showtime
    movie_models = movie_models.Movie

    def get_movie_showtimes(self, movie_id):
        return self.showtime_model.objects.filter(movie_id=movie_id)

    def get_movies(self):
        return self.movie_models.objects.all()

    def get_soon_movies(self, max_days):
        """
        Returns movies that will be soon (premiere) in a month by default.
        """
        return self.movie_models.objects.filter(
            is_active=False,
            start_date__range=(
                (datetime.datetime.now() + datetime.timedelta(days=1)).replace(tzinfo=pytz.UTC),
                (datetime.datetime.now() + datetime.timedelta(days=max_days)).replace(tzinfo=pytz.UTC)
            )
        )
