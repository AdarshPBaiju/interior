# Generated by Django 5.1.1 on 2024-09-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0002_delete_category_delete_contact_delete_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
