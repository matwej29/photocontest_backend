# Generated by Django 4.2.5 on 2023-10-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='avatars', verbose_name='Аватар'),
        ),
    ]
