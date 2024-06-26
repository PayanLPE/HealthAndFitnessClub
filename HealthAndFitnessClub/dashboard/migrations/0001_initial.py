# Generated by Django 5.0.4 on 2024-04-10 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeStaff',
            fields=[
                ('admin_staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'AdministrativeStaff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'db_table': 'Members',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Trainers',
                'managed': False,
            },
        ),
    ]
