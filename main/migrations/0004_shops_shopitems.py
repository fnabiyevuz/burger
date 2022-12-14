# Generated by Django 4.1.1 on 2022-09-23 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_categories_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('opened', 'opened'), ('booked', 'booked'), ('canceled', 'canceled'), ('accepted', 'accepted'), ('sent', 'sent'), ('sold', 'sold')], default='opened', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShopItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shops')),
            ],
        ),
    ]
