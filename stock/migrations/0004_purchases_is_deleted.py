# Generated by Django 4.2.9 on 2024-01-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_remove_purchases_price_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
