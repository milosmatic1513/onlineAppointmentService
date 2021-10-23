from django.urls import path, register_converter
from datetime import datetime
from . import views

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('book/',views.book,name="book_appointment"),
    path('<yyyy:date>/', views.appointment, name='appointment'),
    path('<int:appointment_id>/', views.detail, name='detail'),
]
