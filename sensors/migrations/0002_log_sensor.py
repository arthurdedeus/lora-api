# Generated by Django 3.1.12 on 2021-08-19 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sensors.sensor'),
        ),
    ]