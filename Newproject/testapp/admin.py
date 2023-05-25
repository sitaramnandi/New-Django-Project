from django.contrib import admin
from testapp.models import user

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=["username","password","email",]
    admin.site.register(user)
