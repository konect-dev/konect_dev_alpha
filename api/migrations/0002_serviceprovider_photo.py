# Generated by Django 3.2.4 on 2021-06-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='photo',
            field=models.FileField(blank=True, upload_to='media/photos/service_provider_avatars/'),
        ),
    ]
