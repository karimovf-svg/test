# Generated by Django 5.2 on 2025-04-16 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0002_alter_user_is_active_alter_user_is_student_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Day',
        ),
    ]
