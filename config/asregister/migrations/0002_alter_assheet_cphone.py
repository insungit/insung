# Generated by Django 4.0.4 on 2022-06-03 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asregister', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assheet',
            name='cphone',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(regex='\\d{2,3}-\\d{3,4}-\\d{4}')], verbose_name='연락처'),
        ),
    ]