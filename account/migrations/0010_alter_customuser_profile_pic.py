# Generated by Django 4.2.6 on 2023-11-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_customuser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(max_length=100000, null=True, upload_to=''),
        ),
    ]
