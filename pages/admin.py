from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumb(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))

    thumb.short_description = 'photo'

    list_display = ('id', 'thumb', 'first_name', 'last_name','designation', 'create_date')
    list_display_links = ('first_name','thumb')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
