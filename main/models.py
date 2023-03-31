from django.utils import timezone
from django.db import models


class Bio(models.Model):
    photo = models.ImageField(upload_to='bio_image', null=False, blank=True)
    bio = models.TextField()

    class Meta:
        verbose_name = 'Биография'
        verbose_name_plural = 'Биография'


class Video(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='video_image', null=True, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to='video', null=True, blank=True)

    class Meta:
        verbose_name = 'Видео главной страницы'
        verbose_name_plural = 'Видео главной страницы'


class LastTrack(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField(default=timezone.now)
    track = models.FileField(upload_to='main_tracks')

    class Meta:
        verbose_name = 'Последние трэки'
        verbose_name_plural = 'Последние трэки'
