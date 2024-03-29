# Generated by Django 4.0.3 on 2022-03-21 22:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_messages_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='whatsapp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='threads',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
