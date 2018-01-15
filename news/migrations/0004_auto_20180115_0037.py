# Generated by Django 2.0 on 2018-01-15 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180107_0750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['episode', 'category', 'date']},
        ),
        migrations.AlterField(
            model_name='item',
            name='raw_images',
            field=models.TextField(blank=True, verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='raw_references',
            field=models.TextField(blank=True, verbose_name='references'),
        ),
        migrations.AlterField(
            model_name='item',
            name='raw_sources',
            field=models.TextField(blank=True, verbose_name='sources'),
        ),
    ]
