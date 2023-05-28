from django.contrib import admin

from . import models


class PurchaseHistoryInline(admin.TabularInline):
    model = models.PurchaseHistory
    extra = 1


class TicketInline(admin.TabularInline):
    model = models.Ticket
    extra = 1


class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'date', 'room_id', 'cinema_id', 'tickets_sold')
    list_filter = ('movie_id', 'date', 'room_id', 'cinema_id')
    search_fields = ('movie_id', 'date', 'cinema_id')
    inlines = (TicketInline,)


admin.site.register(models.Ticket)
admin.site.register(models.PurchaseHistory)
admin.site.register(models.Showtime, ShowtimeAdmin)
