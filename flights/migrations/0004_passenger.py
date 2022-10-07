# Generated by Django 4.1 on 2022-10-03 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_airport_alter_flight_destination_alter_flight_origin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight')),
            ],
        ),
    ]