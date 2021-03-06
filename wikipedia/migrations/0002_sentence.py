# Generated by Django 4.0.4 on 2022-04-26 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wikipedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_sentence', models.CharField(max_length=5000)),
                ('translated_sentence', models.CharField(max_length=5000)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wikipedia.project')),
            ],
        ),
    ]
