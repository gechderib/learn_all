# Generated by Django 4.2.6 on 2023-11-27 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_description_and_more'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='postedBy',
        ),
        migrations.RemoveField(
            model_name='item',
            name='subcategory',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.category'),
        ),
    ]