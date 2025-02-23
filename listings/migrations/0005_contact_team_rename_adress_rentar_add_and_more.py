# Generated by Django 5.0.3 on 2024-06-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.TextField()),
                ('M_No', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='rentar',
            old_name='adress',
            new_name='add',
        ),
        migrations.AlterField(
            model_name='details',
            name='Mnumber',
            field=models.CharField(max_length=10),
        ),
    ]
