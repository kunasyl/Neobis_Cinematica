from django.contrib import admin

from . import models


class SeatInline(admin.TabularInline):
    model = models.Seat
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'cinema_id', 'place_count', 'row_count', 'seat_count')
    list_filter = ('cinema_id', )
    search_fields = ('cinema_id', )
    inlines = (SeatInline, )


class RoomInline(admin.TabularInline):
    model = models.Room
    extra = 1


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
    list_filter = ('city', )
    search_fields = ('name', )
    inlines = (RoomInline,)


admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Cinema, CinemaAdmin)
