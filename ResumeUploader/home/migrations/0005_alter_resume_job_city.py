# Generated by Django 3.2.8 on 2021-10-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_resume_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='job_city',
            field=models.CharField(max_length=50),
        ),
    ]