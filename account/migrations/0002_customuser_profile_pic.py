# Generated by Django 4.2.6 on 2023-11-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.CharField(max_length=100, null=True),
        ),
    ]