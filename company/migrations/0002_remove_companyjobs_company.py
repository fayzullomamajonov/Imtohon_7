# Generated by Django 5.0.2 on 2024-03-01 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyjobs',
            name='company',
        ),
    ]
