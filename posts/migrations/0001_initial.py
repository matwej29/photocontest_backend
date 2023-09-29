# Generated by Django 4.2.5 on 2023-09-29 07:00

from django.db import migrations, models
import django.db.models.deletion


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
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='Аватар')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='post_photos', verbose_name='Фото')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Название фото')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('posted_at', models.DateTimeField(default=None, null=True)),
                ('description', models.CharField(max_length=5000, verbose_name='Описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=5000, verbose_name='Комментарий')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
