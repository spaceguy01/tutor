# Generated by Django 2.0.3 on 2018-04-20 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
