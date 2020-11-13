# Generated by Django 3.1.3 on 2020-11-13 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='category',
            name='to_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
