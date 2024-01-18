from django.contrib import admin
from . import models

class AdminArtwork(admin.ModelAdmin):
    list_display = [
        'artwork_id',
        'artist',
        'artwork_name',
        'rating',
    ]

admin.site.register(models.Artwork, AdminArtwork)

class AdminExhibition(admin.ModelAdmin):
    list_display=[
        'exhibition_id',
        'exhibition_name',
        'capacity'
    ]

admin.site.register(models.Exhibition, AdminExhibition)