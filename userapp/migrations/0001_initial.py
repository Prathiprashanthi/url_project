# Generated by Django 4.2.6 on 2023-11-01 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('testurl', models.TextField()),
                ('test_qrcode', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'db_table': 'Testing_Details',
            },
        ),
        migrations.CreateModel(
            name='URLMOdel',
            fields=[
                ('url_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('user_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_url', to='mainapp.usermodel')),
            ],
            options={
                'db_table': 'URL_QR_Details',
            },
        ),
    ]
