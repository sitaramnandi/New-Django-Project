# Generated by Django 4.1 on 2023-06-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Phonenumber', models.CharField(max_length=10)),
                ('Booking_date', models.DateField()),
                ('location', models.CharField(choices=[('HYD', 'Hyderabad')], default='HYD', max_length=100)),
            ],
        ),
    ]
