# Generated by Django 4.2.6 on 2023-11-27 10:22

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_alter_category_description_and_more'),
        ('item', '0010_alter_item_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='item_images/'), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='postedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory'),
        ),
    ]
