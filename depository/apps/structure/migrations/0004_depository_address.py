# Generated by Django 2.2.4 on 2019-08-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0003_auto_20190809_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='depository',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]