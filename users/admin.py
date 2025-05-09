from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ['role']
    readonly_fields = ('last_login', 'date_joined')
    exclude = ['password']

admin.site.register(User, UserAdmin)
