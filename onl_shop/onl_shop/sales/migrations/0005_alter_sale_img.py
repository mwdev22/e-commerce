# Generated by Django 4.2.5 on 2023-12-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_sale_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='img',
            field=models.ImageField(default='sales/sale.png', upload_to='media/sales'),
        ),
    ]
