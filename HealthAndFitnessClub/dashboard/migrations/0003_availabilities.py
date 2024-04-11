# Generated by Django 5.0.4 on 2024-04-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_goals_alter_administrativestaff_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availabilities',
            fields=[
                ('availability_id', models.AutoField(primary_key=True, serialize=False)),
                ('trainer_id', models.IntegerField()),
                ('day', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'db_table': 'availabilities',
                'managed': False,
            },
        ),
    ]