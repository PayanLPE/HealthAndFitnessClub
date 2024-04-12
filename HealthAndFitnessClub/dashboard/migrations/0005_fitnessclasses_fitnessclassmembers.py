# Generated by Django 5.0.4 on 2024-04-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_equipments_roombookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessClasses',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('trainer_id', models.IntegerField()),
                ('class_start_time', models.TimeField()),
                ('class_end_time', models.TimeField()),
            ],
            options={
                'db_table': 'fitnessclasses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FitnessClassMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('member_id', models.IntegerField()),
            ],
            options={
                'db_table': 'fitnessclassmembers',
                'managed': False,
            },
        ),
    ]