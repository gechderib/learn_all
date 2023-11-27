# Generated by Django 4.2.6 on 2023-11-27 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_description_and_more'),
        ('item', '0006_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='category.subcategory'),
        ),
    ]
