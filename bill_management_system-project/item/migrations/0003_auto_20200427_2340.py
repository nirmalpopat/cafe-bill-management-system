# Generated by Django 3.0.5 on 2020-04-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_itemheader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemheader',
            name='itemheader_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
