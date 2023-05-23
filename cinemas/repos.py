from . import models
from showtimes import models as showtime_models


class CinemaRepos:
    model = models.Cinema
    showtime_model = showtime_models.Showtime

    def get_cinemas(self):
        return self.model.objects.all()

    def get_cinema(self, pk):
        return self.model.objects.get(id=pk)

    def get_cinema_showtimes(self, cinema_id):
        return self.showtime_model.objects.filter(cinema_id=cinema_id)

