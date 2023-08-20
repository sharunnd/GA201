# Generated by Django 4.2.4 on 2023-08-19 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.BooleanField(default=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dishes_added', to=settings.AUTH_USER_MODEL)),
                ('customers_favorite', models.ManyToManyField(blank=True, related_name='favorite_dishes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
