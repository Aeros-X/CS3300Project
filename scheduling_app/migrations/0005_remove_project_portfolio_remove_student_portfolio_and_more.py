# Generated by Django 4.2.6 on 2023-11-02 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_app', '0004_rename_work_shift_workshift'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='portfolio',
        ),
        migrations.RemoveField(
            model_name='student',
            name='portfolio',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
