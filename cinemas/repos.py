from . import models


class CinemaRepos:
    model = models.Cinema

    def get_cinemas(self):
        return self.model.objects.all()

    def get_cinema(self, pk):
        return self.model.objects.get(id=pk)
