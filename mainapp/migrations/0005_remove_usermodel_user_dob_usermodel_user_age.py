# Generated by Django 4.2.6 on 2023-11-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_otp_usermodel_otp_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='user_dob',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_age',
            field=models.IntegerField(null=True),
        ),
    ]