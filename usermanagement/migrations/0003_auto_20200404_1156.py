# Generated by Django 2.2.12 on 2020-04-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0002_auto_20200404_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email Address'),
        ),
    ]
