# Generated by Django 3.2.8 on 2021-11-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhut', '0003_alter_measurement_when'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.IntegerField(default=0, verbose_name='Identification of sensor'),
            preserve_default=False,
        ),
    ]
