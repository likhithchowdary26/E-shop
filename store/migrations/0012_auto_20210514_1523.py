# Generated by Django 3.1.7 on 2021-05-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210514_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order12',
            name='unit_price',
            field=models.IntegerField(),
        ),
    ]