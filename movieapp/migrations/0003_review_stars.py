# Generated by Django 4.1.4 on 2023-01-02 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_director_movie_review_delete_directs'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]