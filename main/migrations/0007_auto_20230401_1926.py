# Generated by Django 3.2.14 on 2023-04-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20230331_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galery',
            old_name='photo',
            new_name='photo_4_6',
        ),
        migrations.AddField(
            model_name='galery',
            name='photo_4_6_2',
            field=models.ImageField(blank=True, null=True, upload_to='galery_image'),
        ),
        migrations.AddField(
            model_name='galery',
            name='photo_4_6_3',
            field=models.ImageField(blank=True, null=True, upload_to='galery_image'),
        ),
        migrations.AddField(
            model_name='galery',
            name='photo_5_5',
            field=models.ImageField(blank=True, null=True, upload_to='galery_image'),
        ),
        migrations.AddField(
            model_name='galery',
            name='photo_7_7',
            field=models.ImageField(blank=True, null=True, upload_to='galery_image'),
        ),
    ]
