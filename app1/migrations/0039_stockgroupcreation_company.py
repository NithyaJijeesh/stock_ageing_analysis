# Generated by Django 4.0.5 on 2022-09-29 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0038_remove_stockgroupcreation_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockgroupcreation',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
