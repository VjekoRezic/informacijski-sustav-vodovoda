# Generated by Django 4.0.1 on 2022-01-10 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tiket_statusi', '0001_initial'),
        ('prikljucci', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=50)),
                ('pitanje', models.TextField()),
                ('odgovor', models.TextField(default=None)),
                ('prikljucak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prikljucci.prikljucak')),
                ('racunovodja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiket_statusi.statustiketa')),
            ],
        ),
    ]
