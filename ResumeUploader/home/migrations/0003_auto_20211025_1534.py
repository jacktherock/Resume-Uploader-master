# Generated by Django 3.2.8 on 2021-10-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_resume_my_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='job_city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Nagpur', 'Nagpur'), ('Aurangabad', 'Aurangabad'), ('Nashik', 'Nashik')], max_length=50),
        ),
    ]