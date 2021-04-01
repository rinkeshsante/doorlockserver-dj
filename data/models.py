from django.db import models
from django.contrib.auth import get_user_model


class SUser(models.Model):
    User_Name = models.CharField(max_length=30)
    RFID_No = models.IntegerField()
    Password = models.CharField(max_length=200)
    Facial_Details = models.CharField(max_length=200)

    def __str__(self):
        return self.User_Name


class Room(models.Model):
    Room_Name = models.CharField(max_length=30)
    ip = models.CharField(max_length=200)
    Room_Incharge = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )

    def __str__(self):
        return self.Room_Name


class Permission(models.Model):
    User = models.ForeignKey(
        'SUser',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )
    Room = models.ForeignKey(
        'Room',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )
    Valid_Till = models.DateField()

    def __str__(self):
        return str(self.User) + '->' + str(self.Room)


class RoomEntry(models.Model):
    Permission = models.ForeignKey(
        'Permission',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )
    time_stamp = models.DateTimeField(auto_now_add=True)
    Is_entry = models.BooleanField(default=True)

    def __str__(self):
        return str(self.Permission) + ' at ' + str(self.time_stamp)
