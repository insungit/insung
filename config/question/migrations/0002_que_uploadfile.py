# Generated by Django 4.0.4 on 2022-05-11 14:56

from django.db import migrations, models
import django.db.models.deletion
import question.utils


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='que_UploadFile',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=70, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('uploadedFile', models.FileField(blank=True, upload_to=question.utils.rename_file_to_uuid)),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
                ('menu', models.TextField(blank=True, null=True)),
                ('que_no', models.ForeignKey(db_column='que_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='question.question_sheet')),
            ],
            options={
                'verbose_name': '문의글 첨부파일',
                'verbose_name_plural': '문의글 첨부파일',
                'db_table': 'que_uploadfile',
                'managed': True,
            },
        ),
    ]