# Generated by Django 3.2.4 on 2021-06-22 07:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_serviceprovider_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stutus',
            new_name='Status',
        ),
    ]
