# Generated by Django 4.1.5 on 2023-01-25 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_mrgn_base_uv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mrgn_base_uv',
        ),
    ]