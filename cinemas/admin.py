from django.contrib import admin

from . import models

class RoomInline(admin.TabularInline):
    model = models.Room
    extra = 1


class CinemaAdmin(admin.ModelAdmin):
    # list_display = ('title', 'category', 'price')
    # list_filter = ('category', 'sale')
    # search_fields = ('title', )
    inlines = (RoomInline,)


admin.site.register(models.Room)
admin.site.register(models.Cinema, CinemaAdmin)
