# Generated by Django 3.0.5 on 2020-04-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='numberOfDengue',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='year',
            field=models.IntegerField(),
        ),
    ]