# Generated by Django 4.2.7 on 2024-01-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grabify', '0003_remove_customuser_is_active_customuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
