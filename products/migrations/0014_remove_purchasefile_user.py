# Generated by Django 5.0.2 on 2024-03-19 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_purchasefile_pdf_file_alter_purchasefile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasefile',
            name='user',
        ),
    ]
