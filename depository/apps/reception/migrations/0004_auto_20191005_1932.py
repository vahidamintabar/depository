# Generated by Django 2.2.4 on 2019-10-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_auto_20190909_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='exit_type',
            field=models.IntegerField(blank=True, choices=[(0, 'تحویل به زائر'), (1, 'انتقال به انبار'), (2, 'گم شده')], null=True),
        ),
    ]