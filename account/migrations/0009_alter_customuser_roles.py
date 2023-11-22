# Generated by Django 4.2.6 on 2023-11-20 13:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_customuser_role_customuser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=list, size=None),
        ),
    ]
