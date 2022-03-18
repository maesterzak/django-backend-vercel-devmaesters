# Generated by Django 4.0.3 on 2022-03-18 08:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_author_unique_id_alter_category_unique_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='facebook',
            field=models.CharField(default='undefined', max_length=15),
        ),
        migrations.AddField(
            model_name='author',
            name='instagram',
            field=models.URLField(default='undefined'),
        ),
        migrations.AddField(
            model_name='author',
            name='linkdn',
            field=models.URLField(default='undefined'),
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.URLField(default='undefined'),
        ),
        migrations.AlterField(
            model_name='author',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('f0db859a-4ef2-4c0c-912f-292cb12671fb')),
        ),
        migrations.AlterField(
            model_name='category',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('b78d553a-fc09-4667-8811-20e000dcc27b')),
        ),
        migrations.AlterField(
            model_name='posts',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('27c2bbbf-ce40-4f75-9245-0261531fc9ca')),
        ),
        migrations.AlterField(
            model_name='threads',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('6185b585-ba05-4464-87f3-49e21d5eb761')),
        ),
    ]