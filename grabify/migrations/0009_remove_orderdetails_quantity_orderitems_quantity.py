# Generated by Django 4.2.7 on 2024-01-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grabify', '0008_orderdetails_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='quantity',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
