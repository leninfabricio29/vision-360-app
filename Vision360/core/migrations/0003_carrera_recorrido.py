# Generated by Django 5.0.3 on 2024-03-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bloque_carrera_facultad_foto_remove_booking_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='recorrido',
            field=models.BooleanField(default=False),
        ),
    ]
