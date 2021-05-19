# Generated by Django 3.0.8 on 2020-12-06 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pr1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['pseudonym']},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first',
            new_name='pseudonym',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last',
        ),
    ]
