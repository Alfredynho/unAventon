# Generated by Django 2.0.3 on 2018-05-27 18:56

import datetime
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dominio', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=15)),
                ('capacidad', models.IntegerField()),
                ('esta_activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConversacionPrivada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHora', models.DateTimeField(auto_created=True)),
                ('mensaje', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ConversacionPublica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHoraPregunta', models.DateTimeField(auto_created=True)),
                ('pregunta', models.CharField(max_length=150)),
                ('respuesta', models.CharField(default=None, max_length=150, null=True)),
                ('fechaHoraRespuesta', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CuentaBancaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbu', models.CharField(max_length=25, unique=True)),
                ('entidad', models.CharField(default=None, max_length=20, null=True)),
                ('esta_activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=16, unique=True)),
                ('fechaDeVencimiento', models.CharField(default=None, max_length=5, null=True)),
                ('fechaDeCreacion', models.CharField(default=None, max_length=5, null=True)),
                ('ccv', models.IntegerField()),
                ('esta_activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoViaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('fechaDeNacimiento', models.DateField(default=None, null=True)),
                ('dni', models.CharField(default=None, max_length=15, null=True)),
                ('foto_de_perfil', models.ImageField(default='assets/default-user.png', storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('se_repite', models.CharField(default=None, max_length=50, null=True)),
                ('gasto_total', models.FloatField(default=0.0)),
                ('comentario', models.CharField(max_length=150)),
                ('origen', models.CharField(max_length=20)),
                ('destino', models.CharField(max_length=20)),
                ('fecha_hora_salida', models.DateTimeField()),
                ('duracion', models.FloatField()),
                ('comision', models.FloatField(default=0.05)),
                ('activo', models.BooleanField(default=True)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='unAventonApp.Auto')),
                ('cuenta_bancaria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='unAventonApp.CuentaBancaria')),
            ],
        ),
        migrations.CreateModel(
            name='ViajeCopiloto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_de_solicitud', models.DateTimeField(auto_created=True, default=datetime.datetime(2018, 5, 27, 18, 56, 33, 242707, tzinfo=utc))),
                ('fecha_del_viaje', models.DateTimeField()),
                ('estaConfirmado', models.NullBooleanField(default=None)),
                ('calificacion_a_piloto', models.IntegerField(default=None, null=True)),
                ('calificacion_a_piloto_mensaje', models.CharField(default=None, max_length=150, null=True)),
                ('calificacion_a_copiloto', models.IntegerField(default=None, null=True)),
                ('calificacion_a_copiloto_mensaje', models.CharField(default=None, max_length=150, null=True)),
                ('tarjeta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='unAventonApp.Tarjeta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAventonApp.Usuario')),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAventonApp.Viaje')),
            ],
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='usuario',
            field=models.ManyToManyField(to='unAventonApp.Usuario'),
        ),
        migrations.AddField(
            model_name='cuentabancaria',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAventonApp.Usuario'),
        ),
        migrations.AddField(
            model_name='conversacionpublica',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAventonApp.Usuario'),
        ),
        migrations.AddField(
            model_name='conversacionpublica',
            name='viaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAventonApp.Viaje'),
        ),
        migrations.AddField(
            model_name='conversacionprivada',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAventonApp.Usuario'),
        ),
        migrations.AddField(
            model_name='conversacionprivada',
            name='viaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAventonApp.Viaje'),
        ),
        migrations.AddField(
            model_name='auto',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAventonApp.Usuario'),
        ),
        migrations.AlterUniqueTogether(
            name='viajecopiloto',
            unique_together={('usuario', 'viaje', 'fecha_del_viaje')},
        ),
    ]
