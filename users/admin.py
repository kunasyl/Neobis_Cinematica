from django.contrib import admin

from . import models


class DiscountInline(admin.TabularInline):
    model = models.Discount
    extra = 1


class FeedbackInline(admin.TabularInline):
    model = models.Feedback
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = (DiscountInline, FeedbackInline,)


admin.site.register(models.Discount)
admin.site.register(models.Feedback)
admin.site.register(models.User, UserAdmin)
