# Generated by Django 4.1.4 on 2023-01-02 05:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0004_alter_blog_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]