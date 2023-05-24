from django.contrib import admin

from . import models


class FeedbackInline(admin.TabularInline):
    model = models.Feedback
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = (FeedbackInline,)


admin.site.register(models.Feedback)
admin.site.register(models.User, UserAdmin)
