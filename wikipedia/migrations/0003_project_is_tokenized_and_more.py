# Generated by Django 4.0.4 on 2022-04-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikipedia', '0002_sentence'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_tokenized',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='translated_sentence',
            field=models.CharField(default='No Translation Found', max_length=5000),
        ),
    ]
