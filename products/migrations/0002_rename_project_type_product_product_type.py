# Generated by Django 3.2 on 2022-08-21 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='project_type',
            new_name='product_type',
        ),
    ]