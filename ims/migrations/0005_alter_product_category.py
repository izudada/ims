# Generated by Django 3.2.16 on 2022-12-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0004_auto_20221210_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]