# Generated by Django 4.0.1 on 2022-03-12 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='created_at',
        ),
    ]
