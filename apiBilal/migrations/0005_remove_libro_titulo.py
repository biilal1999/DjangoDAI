# Generated by Django 3.1.4 on 2021-01-04 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiBilal', '0004_auto_20210104_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='titulo',
        ),
    ]