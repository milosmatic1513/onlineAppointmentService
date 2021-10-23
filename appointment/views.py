from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
from django.shortcuts import render

def appointment(request,date):
    appointment_list= Appointment.objects.all().filter(appointment_date=date).order_by('appointment_time');
    context = {
        'weekday':weekdayToString(date.weekday()),
        'day':date.strftime("%d"),
        'month':date.strftime("%m"),
        'year':date.strftime("%Y"),
        'appointment_list': appointment_list,
    }
    return render(request, 'appointment/appointment.html', context)

def detail(request, appointment_id):
    return HttpResponse("You're looking at question %s." % appointment_id)

def book(request):
    context = {}
    return render(request, 'appointment/book_appointment.html', context)
    
def weekdayToString(weekdayNumber):
    return{
        0: 'Monday',
        1: 'Tuesday',
        2:'Wednesday',
        3:'Thursday',
        4:'Friday',
        5:'Saturday',
        6:'Sunday',
        }[weekdayNumber]
