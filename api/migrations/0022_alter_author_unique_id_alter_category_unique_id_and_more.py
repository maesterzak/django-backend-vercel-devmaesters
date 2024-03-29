# Generated by Django 4.0.3 on 2022-03-19 15:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_author_whatsapp_alter_author_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('3a7bbc7b-7932-4aea-aac6-8dae95290b7a')),
        ),
        migrations.AlterField(
            model_name='category',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('50d2e22d-11a7-488d-b1b2-84a11ed480bf')),
        ),
        migrations.AlterField(
            model_name='portfolio_projects',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('8da9cc65-bfb2-4a5d-b7de-b3a2af278739')),
        ),
        migrations.AlterField(
            model_name='threads',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('ac3ffdc2-bbcf-4a52-9f83-d149f22644be')),
        ),
    ]
