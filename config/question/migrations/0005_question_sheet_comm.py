# Generated by Django 4.0.4 on 2022-05-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_alter_question_comment_parent_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_sheet',
            name='comm',
            field=models.PositiveIntegerField(null=True, verbose_name='댓글수'),
        ),
    ]