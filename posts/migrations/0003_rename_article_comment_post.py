# Generated by Django 4.0.8 on 2022-11-15 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='post',
        ),
    ]
