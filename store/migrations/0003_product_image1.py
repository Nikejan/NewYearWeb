# Generated by Django 4.1.4 on 2022-12-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
