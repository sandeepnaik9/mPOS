# Generated by Django 4.1.3 on 2022-11-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0005_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='firstname',
            field=models.TextField(max_length=100),
        ),
    ]
