# Generated by Django 4.1.3 on 2022-11-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_order_quantity_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='TotalBill',
            field=models.CharField(max_length=30),
        ),
    ]