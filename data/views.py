from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import SUser


def index(request):
    res = """<h3>Hello , This application is server for RFID + face detection/ password security system</h3>
    login at ,<a  href="admin">login</a>
    """
    return HttpResponse(res)


def getId(request):
    if request.method == 'POST':
        print('we are using the post method')
    return JsonResponse({'id_exit': False})


def verifyRFID(request):
    if request.method == 'POST':
        # extract data from request---
        data = {}
    rfid_no = data.rfid

    try:
        # check if any student has that rfid no
        student = SUser.objects.get(RFIfacD_No=rfid_no)
        return JsonResponse({'exist': True, 'student_id': student.id})
    except:
        # else return false
        return JsonResponse({'exist': False})


def verifyFACE(request):
    if request.method == 'POST':
        data = {}
    # extract data from request ----
    rfid_no = data.rfid
    face_data = data.Facial_Details
    # check if any student existing face

    try:

        # check if any student have that rfid
        student = SUser.objects.get(RFIfacD_No=rfid_no)

        #  run face detial comparison
        match = student.Facial_Details == face_data
        if match >= 95:
            return JsonResponse({'face_verified': True, 'student_id': student.id})
        else:
            return JsonResponse({'face_verified': False})
    except:
        # else return false
        return JsonResponse({'exist': False})

# Create your tests here.
