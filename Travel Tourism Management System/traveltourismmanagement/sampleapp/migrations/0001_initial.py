# Generated by Django 4.2.10 on 2024-02-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_desig', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student_table',
            },
        ),
    ]
