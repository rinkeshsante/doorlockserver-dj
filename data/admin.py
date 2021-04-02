from django.contrib import admin
from . models import *


class SUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'User_Name', 'RFID_No')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'Room_Name')


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Room', 'Valid_Till')


class RoomEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_stamp', 'Permission', 'Is_entry')


# Register your models here.
admin.site.register(SUser, SUserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(RoomEntry, RoomEntryAdmin)
