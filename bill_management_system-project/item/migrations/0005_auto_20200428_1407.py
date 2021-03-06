# Generated by Django 3.0.5 on 2020-04-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20200428_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemheader',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='itemheader',
            name='itemheader_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
