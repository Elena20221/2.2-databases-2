# Generated by Django 4.1.3 on 2022-11-27 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('created_at', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=50)),
                ('measurements', models.ManyToManyField(related_name='measurements', to='measurement.measurement')),
            ],
        ),
        migrations.CreateModel(
            name='SensorMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основной')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='measurement.measurement')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='measurement.sensor')),
            ],
        ),
    ]
