# Generated by Django 5.0.1 on 2024-01-23 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_promote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile'),
        ),
    ]
