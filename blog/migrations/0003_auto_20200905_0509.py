# Generated by Django 3.1.1 on 2020-09-05 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='post_id',
            new_name='post',
        ),
    ]
