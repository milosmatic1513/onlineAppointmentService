from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
from django.shortcuts import render
from .forms import AppointmentForm
from .models import Appointment,Person
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/authentication/login')
def book(request):
    if request.method =="POST":
        form=AppointmentForm(request.POST)
        if form.is_valid():
            new_appointment = Appointment()
            new_appointment.appointment_status=0
            new_appointment.appointment_time=form.cleaned_data['appointment_time']
            new_appointment.appointment_date=form.cleaned_data['appointment_date']
            print(form.cleaned_data)
            new_appointment.person =     Person()
            print(new_appointment)
    else:
        form=AppointmentForm()

    context = {"form":form}
    return render(request, 'appointment/book_appointment.html', context)

def appointment_form(request):
    form=AppointmentForm()
    context = {"form":form}
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
