from django.contrib import admin
from .models import Video, Bio, LastTrack

admin.site.register(Bio)
admin.site.register(Video)
admin.site.register(LastTrack)
