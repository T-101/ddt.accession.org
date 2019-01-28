from django.contrib import admin

from ddt.models import Registration, Wall


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'handle', 'amount', 'hidden', 'created']


admin.site.register(Registration, RegistrationAdmin)


class WallAdmin(admin.ModelAdmin):
    list_display = ['pk', 'handle', 'text', 'created']


admin.site.register(Wall, WallAdmin)
