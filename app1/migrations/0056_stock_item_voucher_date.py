# Generated by Django 4.1 on 2022-10-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0055_alter_stock_item_voucher_voucher_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_item_voucher',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
