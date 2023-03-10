# Generated by Django 4.0.3 on 2022-03-21 08:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание новостей'),
        ),
        migrations.AddField(
            model_name='news',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание новостей'),
        ),
        migrations.AddField(
            model_name='news',
            name='slug_en',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug_ru',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок новостей'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок новостей'),
        ),
    ]
