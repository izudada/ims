# Generated by Django 3.2.16 on 2022-12-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='size',
            field=models.CharField(max_length=200, null=True),
        ),
    ]