# Generated by Django 4.0.4 on 2022-06-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isscm', '0007_product_management_info_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_management',
            name='current_location',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='현재 위치'),
        ),
        migrations.AlterField(
            model_name='product_management',
            name='serial',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='시리얼'),
        ),
        migrations.AlterField(
            model_name='product_management',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='상태'),
        ),
    ]
