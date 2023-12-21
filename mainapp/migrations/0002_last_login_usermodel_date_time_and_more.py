# Generated by Django 4.2.6 on 2023-11-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Last_login',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Login_Time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'last_login',
            },
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Date_Time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Last_Login_Date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Last_Login_Time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Message',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='No_Of_Times_Login',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Otp_Num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='Otp_Status',
            field=models.TextField(default='pending', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='User_Status',
            field=models.TextField(default='pending', max_length=50, null=True),
        ),
    ]