from django import forms
from .models import Appointment
TIMES_ENUM = (
    (1,'08:00'),
    (2,'08:30'),
    (3,'09:00'),
    (4,'09:30'),
    (5,'10:00'),
    (6,'10:30'),
    (7,'11:00'),
    (8,'11:30'),
    (9,'12:00'),
    (10,'12:30'),
    (11,'13:00'),
    (12,'13:30'),
    (13,'14:00'),
    (14,'14:30'),
    (15,'15:00'),
    (16,'15:30'),
    (17,'16:00'),
    (18,'16:30'),
    (19,'17:00'),
    (20,'17:30'),
    (21,'18:00'),
    (22,'18:30'),
    (23,'19:00'),
    (24,'19:30'),
    (25,'20:00'),
    (26,'20:30'),
    (27,'21:00'),
    (28,'21:30'),
    (29,'22:00'),
)

class AppointmentForm(forms.Form):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment_time =forms.TypedChoiceField(choices=TIMES_ENUM,coerce=int)
