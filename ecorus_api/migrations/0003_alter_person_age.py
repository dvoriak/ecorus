# Generated by Django 4.0.3 on 2022-03-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecorus_api', '0002_remove_office_people_working_office_people_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
