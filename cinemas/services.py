from . import repos


class CinemaServices:
    repos = repos.CinemaRepos()

    def get_cinemas(self):
        return self.repos.get_cinemas()

    def get_cinema(self, pk):
        return self.repos.get_cinema(pk=pk)

    def get_cinema_showtimes(self, cinema_id):
        return self.repos.get_cinema_showtimes(cinema_id=cinema_id)
