from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(SUser)
admin.site.register(Room)
admin.site.register(Permission)
admin.site.register(RoomEntry)
