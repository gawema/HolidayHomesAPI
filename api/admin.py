from django.contrib import admin

from .models import *

admin.site.register(House)
admin.site.register(Booking)
admin.site.register(Facility)
admin.site.register(HouseFacility)
admin.site.register(Gallery)