# Generated by Django 4.1.5 on 2023-01-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_mrgn_base_uv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mrgn_base_uv',
            field=models.IntegerField(null=True, verbose_name='MRGN_BASE_UV'),
        ),
    ]