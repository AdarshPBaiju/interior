# Generated by Django 5.1.1 on 2024-09-09 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
