# Generated by Django 3.2.9 on 2022-01-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('t', 'Top Wear'), ('b', 'Bottom Wear'), ('f', 'Foot Wear')], max_length=1),
        ),
    ]
