# Generated by Django 4.0.8 on 2022-11-21 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank='true', upload_to='screenshots'),
        ),
    ]
