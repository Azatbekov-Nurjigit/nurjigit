# Generated by Django 4.1.4 on 2023-01-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_alter_review_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(),
        ),
    ]