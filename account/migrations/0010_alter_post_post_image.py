# Generated by Django 5.0.3 on 2024-05-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
