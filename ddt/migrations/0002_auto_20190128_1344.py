# Generated by Django 2.1.5 on 2019-01-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wall',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
