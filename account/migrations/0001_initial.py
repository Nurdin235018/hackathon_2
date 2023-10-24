# Generated by Django 4.2.6 on 2023-10-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('activation_code', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
