# Generated by Django 3.1.3 on 2020-11-16 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20201116_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='priec',
            new_name='price',
        ),
    ]