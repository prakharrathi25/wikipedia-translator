# Generated by Django 4.0.4 on 2022-04-27 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikipedia', '0005_project_annotator_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='annotator_id',
            new_name='annotator',
        ),
    ]