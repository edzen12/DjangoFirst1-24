from django.contrib import admin
from apps.about.models import About, Team, SocialLink, ImageShotsTeam


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

class ImageShotsInline(admin.TabularInline):
    model = ImageShotsTeam
    extra = 2


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position'] 
    inlines = [SocialLinkInline, ImageShotsInline]
    prepopulated_fields = {'slug':['name']}


admin.site.register(About)
