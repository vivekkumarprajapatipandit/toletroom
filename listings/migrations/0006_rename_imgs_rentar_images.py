# Generated by Django 5.0.3 on 2024-06-16 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_contact_team_rename_adress_rentar_add_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentar',
            old_name='imgs',
            new_name='images',
        ),
    ]
