# Generated by Django 3.0.5 on 2020-04-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_auto_20200423_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Year', models.CharField(max_length=100)),
                ('Month', models.CharField(max_length=100)),
                ('NumberOfDengueCase', models.CharField(max_length=100)),
                ('MOHOffice', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dataform',
            },
        ),
    ]
