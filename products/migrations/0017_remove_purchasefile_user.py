# Generated by Django 5.0.2 on 2024-04-26 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_purchasefile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasefile',
            name='user',
        ),
    ]
