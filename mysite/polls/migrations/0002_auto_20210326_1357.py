# Generated by Django 3.1.5 on 2021-03-26 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='survey',
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
    ]
