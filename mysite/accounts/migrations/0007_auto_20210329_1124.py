# Generated by Django 3.1.5 on 2021-03-29 02:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20210329_1033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]
