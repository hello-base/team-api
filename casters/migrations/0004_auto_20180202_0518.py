# Generated by Django 2.0 on 2018-02-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casters', '0003_caster_biography'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caster',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='caster',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
