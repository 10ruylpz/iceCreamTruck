# Generated by Django 2.1.2 on 2018-11-30 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20181120_0118'),
        ('orders', '0002_auto_20181130_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderform',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='customers.Customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderform',
            name='flavor',
            field=models.IntegerField(default=0),
        ),
    ]