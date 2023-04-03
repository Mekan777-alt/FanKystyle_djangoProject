# Generated by Django 3.2.14 on 2023-03-31 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('track', models.FileField(upload_to='tracks')),
            ],
            options={
                'verbose_name': 'Трэки',
                'verbose_name_plural': 'Трэки',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='video_image')),
                ('description', models.CharField(max_length=256)),
                ('video', models.FileField(upload_to='videos')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]