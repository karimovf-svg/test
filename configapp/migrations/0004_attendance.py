# Generated by Django 5.2 on 2025-04-19 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0003_delete_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.groupstudent')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.student')),
            ],
        ),
    ]
