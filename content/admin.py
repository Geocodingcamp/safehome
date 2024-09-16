from django.contrib import admin
from .models import *

# Register your models here.
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader')
    filter_horizontal = ('members',)

admin.site.register(ForRent)
admin.site.register(ForSale)
admin.site.register(UserGroup, UserGroupAdmin)