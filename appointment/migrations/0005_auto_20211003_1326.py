# Generated by Django 3.2.6 on 2021-10-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_appointment_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_address',
            field=models.CharField(default='adddress', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_phonenumber',
            field=models.CharField(max_length=12),
        ),
    ]
