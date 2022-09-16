# Generated by Django 3.2.15 on 2022-09-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='excerpt',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='ingredients',
        ),
        migrations.AddField(
            model_name='post',
            name='instructions',
            field=models.TextField(default=''),
        ),
    ]