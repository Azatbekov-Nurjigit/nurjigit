# Generated by Django 4.1.4 on 2023-01-03 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0007_coment_name_stars_delete_director_alter_movie_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='name',
            old_name='text',
            new_name='name',
        ),
    ]
