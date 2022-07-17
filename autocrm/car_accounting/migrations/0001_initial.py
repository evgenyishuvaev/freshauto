# Generated by Django 4.0.5 on 2022-07-17 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'mark',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, unique=True)),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_accounting.mark', to_field='mark')),
            ],
            options={
                'db_table': 'model',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(db_index=True, max_length=9)),
                ('release_year', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('re_registration', models.BooleanField()),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_accounting.mark', to_field='mark')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_accounting.model', to_field='model')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'car',
            },
        ),
    ]
