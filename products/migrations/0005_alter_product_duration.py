# Generated by Django 5.0 on 2024-01-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='duration',
            field=models.CharField(max_length=255),
        ),
    ]
