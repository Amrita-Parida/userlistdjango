# Generated by Django 2.2.12 on 2020-04-04 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0003_auto_20200404_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='email',
        ),
    ]
