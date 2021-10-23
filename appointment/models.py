from django.db import models

# Create your models here.
class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_phonenumber=models.IntegerField()
    person_address=models.CharField(max_length=200);
    person_phonenumber=models.CharField(max_length=12)
    def __str__(self):
            return self.person_name
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
STATUS_ENUM=(
    (0,'PENDING'),
    (1,'FINISHED'),
    (2,'CANCELED')
)
class Appointment(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE,null=True)
    appointment_date = models.DateField('appointment date')
    appointment_time =models.IntegerField(default=1, choices=TIMES_ENUM)
    appointment_status= models.IntegerField(default=0,choices=STATUS_ENUM)
    def __str__(self):
            return self.person.person_name + " " +  self.appointment_date.strftime("%m/%d/%Y, %H:%M")
