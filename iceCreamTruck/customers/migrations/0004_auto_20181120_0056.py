# Generated by Django 2.1.2 on 2018-11-20 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20181120_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_first',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_last',
            new_name='last_Name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_state',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_street',
            new_name='street_Address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_zip',
            new_name='zip_Code',
        ),
    ]
