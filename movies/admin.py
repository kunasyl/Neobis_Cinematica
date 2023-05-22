from django.contrib import admin

from . import models


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'start_date', 'end_date')
    list_filter = ('is_active', )
    search_fields = ('title', 'age_rate',)


admin.site.register(models.Movie, MovieAdmin)
