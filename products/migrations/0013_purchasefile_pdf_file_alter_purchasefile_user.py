# Generated by Django 5.0.2 on 2024-03-18 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_product_pdf_file_alter_category_type_swimmer_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasefile',
            name='pdf_file',
            field=models.FileField(default=1, upload_to='product/product_pdf/', verbose_name='Product PDF File'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchasefile',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_files', to=settings.AUTH_USER_MODEL),
        ),
    ]
