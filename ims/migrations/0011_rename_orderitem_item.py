# Generated by Django 3.2.16 on 2022-12-13 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0010_order_orderitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='Item',
        ),
    ]
