# Generated by Django 4.0.4 on 2022-04-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikipedia', '0007_alter_sentence_translated_sentence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='translated_sentence',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
