# Generated by Django 4.2.5 on 2023-10-13 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0002_sale_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bought', to=settings.AUTH_USER_MODEL)),
                ('sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction', to='sales.sale')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sold', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
