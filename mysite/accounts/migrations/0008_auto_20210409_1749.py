# Generated by Django 3.1.7 on 2021-04-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210329_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
