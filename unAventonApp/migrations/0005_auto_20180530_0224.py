# Generated by Django 2.0.3 on 2018-05-30 02:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('unAventonApp', '0004_auto_20180530_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='ccv',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='numero',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='viajecopiloto',
            name='fecha_hora_de_solicitud',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2018, 5, 30, 2, 24, 46, 856137, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='tarjeta',
            unique_together={('usuario', 'numero')},
        ),
    ]
