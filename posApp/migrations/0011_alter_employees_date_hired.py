# Generated by Django 4.1.3 on 2022-11-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0010_rename_firstname_employees_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='date_hired',
            field=models.DateField(auto_now=True),
        ),
    ]
