# Generated by Django 4.2.7 on 2023-11-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuatomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=200)),
                ('incharge_name', models.CharField(max_length=100)),
                ('incharge_email', models.EmailField(max_length=200)),
                ('GSTIN', models.CharField(max_length=100)),
                ('customer_relationship_start_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
