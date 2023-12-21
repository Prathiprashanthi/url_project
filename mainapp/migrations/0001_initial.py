# Generated by Django 4.2.6 on 2023-11-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(help_text='user_name', max_length=50)),
                ('user_dob', models.DateField(help_text='user_dob', max_length=50, null=True)),
                ('user_email', models.EmailField(help_text='user_email', max_length=254)),
                ('user_password', models.EmailField(help_text='user_password', max_length=50)),
                ('user_address', models.TextField(help_text='user_address', max_length=100)),
                ('user_contact', models.CharField(help_text='user_contact', max_length=15)),
                ('user_image', models.ImageField(null=True, upload_to='media/')),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]