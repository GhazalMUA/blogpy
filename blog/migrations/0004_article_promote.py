# Generated by Django 5.0.1 on 2024-01-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='promote',
            field=models.BooleanField(default=False),
        ),
    ]
