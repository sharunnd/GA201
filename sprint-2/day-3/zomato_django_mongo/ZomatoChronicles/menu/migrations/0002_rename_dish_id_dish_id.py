# Generated by Django 4.1.10 on 2023-08-11 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='dish_id',
            new_name='id',
        ),
        
    ]

