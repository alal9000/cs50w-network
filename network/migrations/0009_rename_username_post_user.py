# Generated by Django 4.0.3 on 2022-05-07 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_remove_post_likes_post_likes_delete_character_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='user',
        ),
    ]
