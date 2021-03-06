# Generated by Django 3.0.5 on 2020-05-20 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField()),
                ('order', models.FloatField(default=1)),
                ('is_asc', models.NullBooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Constant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Depository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('code', models.IntegerField()),
                ('printer_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(default=1)),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='structure.Cabinet')),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(default=1)),
                ('is_healthy', models.BooleanField(default=True)),
                ('size', models.IntegerField(choices=[(0, 'کوچک'), (1, 'بزرگ')], default=0)),
                ('is_fav', models.BooleanField(default=False)),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='structure.Row')),
            ],
        ),
        migrations.AddField(
            model_name='cabinet',
            name='depository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Depository'),
        ),
    ]
