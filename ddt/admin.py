from django.contrib import admin

from ddt.models import Registration, Wall, SiteSettings


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'handle', 'amount', 'hidden', 'created']


admin.site.register(Registration, RegistrationAdmin)


class WallAdmin(admin.ModelAdmin):
    list_display = ['pk', 'handle', 'text', 'created']


admin.site.register(Wall, WallAdmin)


class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'registration_open', 'wall_open']


admin.site.register(SiteSettings, SiteSettingsAdmin)
