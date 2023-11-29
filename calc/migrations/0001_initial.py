# Generated by Django 4.2.7 on 2023-11-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('descri', models.TextField(default='Default description')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
