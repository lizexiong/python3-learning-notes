# Generated by Django 3.2 on 2023-05-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arya', '0002_host_os_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
