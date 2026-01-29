from django.contrib import admin
from apps.about.models import About, Team, SocialLink


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position'] 
    inlines = [SocialLinkInline]


admin.site.register(About)
