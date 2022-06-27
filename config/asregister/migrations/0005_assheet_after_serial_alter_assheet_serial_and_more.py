# Generated by Django 4.0.4 on 2022-06-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asregister', '0004_alter_assheet_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='assheet',
            name='after_serial',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='후 시리얼'),
        ),
        migrations.AlterField(
            model_name='assheet',
            name='serial',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='전 시리얼'),
        ),
        migrations.AlterField(
            model_name='assheet',
            name='site',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='프로젝트명'),
        ),
    ]
