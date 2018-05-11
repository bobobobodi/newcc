from django.contrib import admin
from .models import Transuser

class UserAdmin(admin.ModelAdmin):

    list_display = [
        'qiwi',
        'money_off',
        'money_on',
        'date_off',
        'date_on',
        'tarif',
    ]

admin.site.register(Transuser, UserAdmin)
