# Generated by Django 4.0.3 on 2022-03-18 13:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_author_unique_id_alter_category_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('33ec5355-0044-4476-9a9f-01c5531d37c4')),
        ),
        migrations.AlterField(
            model_name='category',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('92239f12-5a10-45db-8b79-41bdeaf0b730')),
        ),
        migrations.AlterField(
            model_name='posts',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('51d2b1b0-3331-47a1-b8f9-5a9b90af5a33')),
        ),
        migrations.AlterField(
            model_name='threads',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('c857eb25-59bf-42c3-8152-ce14343c3461')),
        ),
    ]
