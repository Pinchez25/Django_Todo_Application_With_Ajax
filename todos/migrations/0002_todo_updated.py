# Generated by Django 4.0.6 on 2022-08-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
