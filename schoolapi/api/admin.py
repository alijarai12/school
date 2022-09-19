from cProfile import Profile
from django.contrib import admin
from api.models import SchoolProfile

# Register your models here.
@admin.register(SchoolProfile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'schoolname', 'schooladdress', 'contact', 'pimage']
