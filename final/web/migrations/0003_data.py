# Generated by Django 3.0.5 on 2020-04-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200421_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField(max_length=20)),
                ('Month', models.TextField()),
                ('numberOfDengue', models.IntegerField(max_length=50)),
                ('MOHoffice', models.TextField()),
            ],
        ),
    ]