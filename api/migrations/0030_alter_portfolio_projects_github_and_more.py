# Generated by Django 4.0.3 on 2022-03-27 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_author_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio_projects',
            name='github',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio_projects',
            name='video',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
