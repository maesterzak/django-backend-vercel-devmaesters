# Generated by Django 4.0.3 on 2022-03-21 01:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_portfolio_projects_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
