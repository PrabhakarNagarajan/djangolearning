# Generated by Django 4.2.7 on 2023-11-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_cuatomer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cuatomer',
            new_name='Customer',
        ),
    ]