# Generated by Django 4.2.7 on 2024-01-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0008_offer_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('XS', 'XS'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=10, null=True),
        ),
    ]
