# Generated by Django 3.1.4 on 2020-12-03 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='to_book',
        ),
    ]
