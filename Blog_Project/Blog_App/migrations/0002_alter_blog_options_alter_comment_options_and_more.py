# Generated by Django 4.1.4 on 2023-01-02 05:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name="What's on your mind?"),
        ),
    ]
