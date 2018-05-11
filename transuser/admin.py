from django.contrib import admin
from .models import Transfer

class UserAdmin(admin.ModelAdmin):

    list_display = [
        'author',
        'money',
        'money_off',
        'date_off',
        'tarif',
    ]

admin.site.register(Transfer, UserAdmin)
