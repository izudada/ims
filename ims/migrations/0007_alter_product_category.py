# Generated by Django 3.2.16 on 2022-12-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0006_alter_label_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]
