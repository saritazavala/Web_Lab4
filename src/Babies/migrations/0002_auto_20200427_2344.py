# Generated by Django 3.0.5 on 2020-04-27 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Babies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baby',
            old_name='lasName',
            new_name='lastName',
        ),
    ]
