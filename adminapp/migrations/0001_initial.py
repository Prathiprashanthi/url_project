# Generated by Django 4.2.6 on 2023-11-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_set', models.FileField(upload_to='files/')),
                ('Accuracy', models.FloatField(null=True)),
                ('Precision', models.FloatField(null=True)),
                ('Recall', models.FloatField(null=True)),
                ('F1_Score', models.FloatField(null=True)),
                ('algo', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'dataset',
            },
        ),
    ]