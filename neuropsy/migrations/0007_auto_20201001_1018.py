# Generated by Django 3.1.1 on 2020-10-01 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neuropsy', '0006_auto_20201001_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neuropsy.order'),
        ),
    ]
