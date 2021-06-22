# Generated by Django 3.2.4 on 2021-06-17 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Stutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('owner_username', models.CharField(blank=True, max_length=32)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(blank=True, choices=[('wiring', 'Car wiring'), ('alignment', 'Wheel Alignment'), ('electrics', 'Electric Cars'), ('engines', 'Engine Checking'), ('wheel_balancing', 'Wheel Balancing'), ('flat_tyres', 'Flat Tyres'), ('computer_aided_mechanics', 'Computer Aided Mechanics')], max_length=32)),
                ('owner_username', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, choices=[('kampala', 'Kampala'), ('kayinga', 'Kayinga'), ('kakiri', 'Kakiri'), ('Nsambya', 'Nsambya'), ('Entebbe', 'Entebbe'), ('Munyonyo', 'Munyonyo'), ('Kiboga', 'Kiboga'), ('Mityana', 'Mityana'), ('Lugazi', 'Lugazi'), ('Kamuli', 'Kamuli'), ('Iganga', 'Iganga'), ('Kitgum', 'Kitgum'), ('Mbarara', 'Mbarara'), ('Gulu', 'Gulu')], max_length=32)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('other', models.CharField(max_length=10000)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
