# Generated by Django 4.2.4 on 2023-09-10 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_alter_car_doors_alter_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='', max_length=1),
        ),
    ]
