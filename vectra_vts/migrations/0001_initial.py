# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_agreement_file', models.FileField(blank=True, upload_to='agreement_files')),
            ],
        ),
        migrations.CreateModel(
            name='GpsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latituide_pos', models.FloatField(default=0.0)),
                ('longtuide_pos', models.FloatField(default=0.0)),
                ('bearing', models.FloatField(default=0.0)),
                ('time_stamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GpsDevice',
            fields=[
                ('device_id', models.CharField(default='123456789', max_length=20, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('A', 'active'), ('D', 'not active')], max_length=2)),
                ('being_used', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], max_length=2)),
                ('activated_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=2)),
                ('birthday', models.DateField(blank=True)),
                ('tel', models.CharField(max_length=14)),
                ('address', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='profile_images')),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('salt', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vectra_vts.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('maker', models.CharField(default='', max_length=50)),
                ('v_model', models.CharField(default='', max_length=50)),
                ('engine', models.CharField(default='', max_length=50)),
                ('color', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='Vehicle_images')),
                ('status', models.CharField(choices=[('A', 'active'), ('D', 'not active')], max_length=2)),
                ('net_weight', models.FloatField(default=0.0)),
                ('fuel_type', models.CharField(max_length=100)),
                ('plate_number', models.CharField(max_length=20)),
                ('made_year', models.DateField()),
                ('gps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vectra_vts.GpsDevice')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vectra_vts.Users')),
            ],
        ),
        migrations.AddField(
            model_name='gpsdata',
            name='gps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vectra_vts.GpsDevice'),
        ),
        migrations.AddField(
            model_name='driver',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vectra_vts.Person'),
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vectra_vts.Users'),
        ),
        migrations.AddField(
            model_name='assignedto',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vectra_vts.Driver'),
        ),
        migrations.AddField(
            model_name='assignedto',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vectra_vts.Vehicle'),
        ),
    ]
