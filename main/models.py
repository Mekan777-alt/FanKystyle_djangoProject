from django.utils import timezone
from django.db import models


class Bio(models.Model):
    photo = models.ImageField(upload_to='bio_image', null=False, blank=True)
    bio = models.TextField()

    class Meta:
        verbose_name = 'Биография'
        verbose_name_plural = 'Биография'

    def __str__(self):
        return 'Биография главной страницы'


class Video(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    video = models.FileField(upload_to='video', null=True, blank=True)
    name1 = models.CharField(max_length=256, default='now')
    description1 = models.TextField(null=True)
    video1 = models.FileField(upload_to='video', null=True, blank=True)
    name2 = models.CharField(max_length=256, default='now')
    description2 = models.TextField(null=True)
    video2 = models.FileField(upload_to='video', null=True, blank=True)
    name3 = models.CharField(max_length=256, default='now')
    description3 = models.TextField(null=True)
    video3 = models.FileField(upload_to='video', null=True, blank=True)
    name4 = models.CharField(max_length=256, default='now')
    description4 = models.TextField(null=True)
    video4 = models.FileField(upload_to='video', null=True, blank=True)

    class Meta:
        verbose_name = 'Видео главной страницы'
        verbose_name_plural = 'Видео главной страницы'

    def __str__(self):
        return f'{self.name} - {self.video}'


class LastTrack(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField(default=timezone.now)
    track = models.FileField(upload_to='main_tracks')

    class Meta:
        verbose_name = 'Последние трэки'
        verbose_name_plural = 'Последние трэки'

    def __str__(self):
        return f'{self.name} - {self.track}'


class Galery(models.Model):
    photo_5_5 = models.ImageField(upload_to='galery_image', null=True, blank=True)
    photo_7_7 = models.ImageField(upload_to='galery_image', null=True, blank=True)
    photo_4_6 = models.ImageField(upload_to='galery_image', null=True, blank=True)
    photo_4_6_2 = models.ImageField(upload_to='galery_image', null=True, blank=True)
    photo_4_6_3 = models.ImageField(upload_to='galery_image', null=True, blank=True)

    class Meta:
        verbose_name = 'Галерея фотографий'
        verbose_name_plural = 'Галерея фотографий'

    def __str__(self):
        return 'Галерея фотографий главной страницы'
