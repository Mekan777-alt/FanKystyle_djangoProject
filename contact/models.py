from django.db import models


class Contact(models.Model):
    message = models.TextField()
    user_name = models.CharField(max_length=100)
    email = models.TextField()
    subject = models.TextField()

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
