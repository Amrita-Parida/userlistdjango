# Generated by Django 2.2.12 on 2020-04-04 11:28

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('real_name', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-Z_ ]*$', 'Invalid characters')], verbose_name='First Name')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super User')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'User Management',
            },
        ),
    ]
