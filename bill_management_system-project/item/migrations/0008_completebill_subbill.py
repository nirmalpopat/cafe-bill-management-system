# Generated by Django 3.0.5 on 2020-05-06 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_customer_detail_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_qty', models.IntegerField()),
                ('item_price', models.IntegerField()),
                ('item_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CompleteBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField()),
                ('c_name', models.CharField(max_length=50)),
                ('c_mono', models.CharField(max_length=50)),
                ('bill_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.SubBill')),
            ],
        ),
    ]
