# Generated by Django 4.2.6 on 2023-12-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('avatar', models.ImageField(default=None, null=True, upload_to='avatars', verbose_name='Аватар')),
                ('token', models.CharField(max_length=100, null=True, verbose_name='Токен')),
                ('expiration_date', models.DateTimeField(null=True, verbose_name='Дата истечения токена')),
                ('registration_token', models.CharField(max_length=50, null=True, verbose_name='Регистрационный токен')),
                ('registration_token_expiration_date', models.DateTimeField(null=True, verbose_name='Дата истечения токена регистрации')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['name'],
            },
        ),
    ]