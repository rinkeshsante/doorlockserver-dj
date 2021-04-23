from django.shortcuts import render
import json

from django.http import HttpResponse, JsonResponse
from .models import SUser, Permission, RoomEntry
from .face import compareFacePoinst, makeFacePoints


def index(request):
    return render(request, 'home.html')


def dashBaord(request):
    return render(request, 'data/dashboard.html')


def verifySystem(request):
    return JsonResponse({'live': True})


def verifyRFID(request):
    # input {"rfid":100 ,"room_no":2}
    try:
        # extract data from request---
        data = json.loads(request.body)
        rfid_no = data['rfid']
        room_no = data['room_no']

        # check if any student has that rfid no.
        student = SUser.objects.get(RFID_No=rfid_no)

        # check if he has pesrmssion
        permission = Permission.objects.filter(User=student, Room=room_no)[0]

        # print(permission)

        if permission:  # he has permisson
            last = RoomEntry.objects.filter(
                Permission=permission).order_by('-id')[0]

            if last.Is_entry:  # if he is inside the lab
                entry_log = RoomEntry(Is_entry=False, Permission=permission)
                entry_log.save()
                return JsonResponse({'exist': True, 'student_id': student.id, 'is_inside': True})
            else:  # outside the lab
                entry_log = RoomEntry(Is_entry=True, Permission=permission)
                entry_log.save()
                return JsonResponse({'exist': True, 'student_id': student.id, 'is_inside': False})

        else:  # no persmission

            return JsonResponse({'exist': False})
    except:
        # error
        return JsonResponse({'exist': False})


# rewrite this code here
def verifyFACE(request):
    # input {"student_id":123 ,'is_new':false} , face photo
    try:
        # extract data from request---
        data = json.loads(request.body)
        student_id = data['student_id']
        is_new = data['is_new']
        # get image here
        image = data['face']
        ipFace = makeFacePoints(image)

        student = SUser.objects.get(id=student_id)

        if is_new:
            student.Facial_Details = ipFace
            student.save()
            return JsonResponse({'face_verified': False, 'face_added': True})

        dbFace = student.Facial_Details

        result = compareFacePoinst(ipFace, dbFace)

        if result >= .95:
            return JsonResponse({'face_verified': True})
        else:
            return JsonResponse({'face_verified': False})
    except:
        # else return false
        return JsonResponse({'face_verified': False})
