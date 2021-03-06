# Generated by Django 3.1.3 on 2020-11-13 11:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('priec', models.IntegerField()),
                ('description', models.TextField(max_length=10000)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='property/')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room_image/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_image', to='property.room')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('from_date', models.DateField(default=datetime.datetime(2020, 11, 13, 11, 40, 26, 669636, tzinfo=utc))),
                ('to_date', models.DateField(default=datetime.datetime(2020, 11, 13, 11, 40, 26, 669636, tzinfo=utc))),
                ('Guest', models.IntegerField(default=1)),
                ('children', models.IntegerField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_review', to='property.room')),
            ],
        ),
    ]
