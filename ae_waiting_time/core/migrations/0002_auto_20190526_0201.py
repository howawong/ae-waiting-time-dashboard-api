# Generated by Django 2.0 on 2019-05-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='en_name',
            field=models.CharField(max_length=100),
        ),
    ]
