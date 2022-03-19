# Generated by Django 4.0.3 on 2022-03-19 15:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_author_unique_id_alter_category_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('917d93f3-6acf-4255-919d-38b17fa2c0fb')),
        ),
        migrations.AlterField(
            model_name='category',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('4bb3ccb3-4ae9-4294-9411-9f1e24672ed6')),
        ),
        migrations.AlterField(
            model_name='posts',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('95460c0d-6397-42e4-a130-586e106f0d88')),
        ),
        migrations.AlterField(
            model_name='threads',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('d9b1a925-f73e-4880-a5a8-085d79789f99')),
        ),
    ]
