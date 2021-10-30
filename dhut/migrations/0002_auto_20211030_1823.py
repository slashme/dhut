# Generated by Django 3.2.8 on 2021-10-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhut', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('temp', models.FloatField(verbose_name='Temperature in Celsius')),
                ('rh', models.FloatField(verbose_name='Relative humidity in %')),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]