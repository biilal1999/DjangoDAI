# Generated by Django 3.1.4 on 2021-01-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiBilal', '0005_remove_libro_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='titulo',
            field=models.CharField(default='algo', max_length=200),
            preserve_default=False,
        ),
    ]
