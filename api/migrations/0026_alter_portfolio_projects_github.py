# Generated by Django 4.0.3 on 2022-03-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_remove_author_unique_id_remove_category_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio_projects',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
