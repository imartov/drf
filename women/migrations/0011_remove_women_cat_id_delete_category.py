# Generated by Django 4.1.3 on 2022-11-13 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0010_rename_cat_women_cat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='women',
            name='cat_id',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
