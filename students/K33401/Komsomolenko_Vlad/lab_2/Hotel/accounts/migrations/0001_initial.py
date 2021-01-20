# Generated by Django 3.1.2 on 2020-10-11 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='5', max_length=15)),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('standard', 'standard'), ('improved', 'improved'), ('luxury', 'luxury')], default='standard', max_length=15)),
                ('cost', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('conveniences', models.CharField(max_length=50)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('generated', 'generated'), ('confirmed', 'confirmed'), ('refused', 'refused'), ('completed', 'completed')], default='generated', max_length=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hotel')),
            ],
        ),
    ]