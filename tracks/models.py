from django.db import models
from django.utils import timezone


class Tracks(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField(default=timezone.now)
    track = models.FileField(upload_to='tracks')

    class Meta:
        verbose_name = 'Трэки'
        verbose_name_plural = 'Трэки'


class Video(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='video_image', null=True, blank=True)
    description = models.CharField(max_length=256)
    video = models.FileField(upload_to='videos')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


