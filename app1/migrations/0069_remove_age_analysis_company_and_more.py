# Generated by Django 4.1 on 2022-12-13 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0068_stock_item_voucher_per_stock_item_voucher_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='age_analysis',
            name='company',
        ),
        migrations.RemoveField(
            model_name='age_analysis',
            name='group',
        ),
        migrations.RemoveField(
            model_name='age_analysis',
            name='negative_stock',
        ),
        migrations.RemoveField(
            model_name='age_analysis',
            name='total_qty',
        ),
        migrations.RemoveField(
            model_name='age_analysis',
            name='total_val',
        ),
    ]
