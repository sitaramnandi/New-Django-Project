from django.contrib import admin
from testapp.models import user,ContactUs,bookModel

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=["username","password","email",]
admin.site.register(user)

class ContactUsAdmin(admin.ModelAdmin):
   
    list_display=["username","Email","comments"]
admin.site.register(ContactUs,ContactUsAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display=["Fullname","Email","Phonenumber","Booking_date","location"]
admin.site.register(bookModel,BookingAdmin)