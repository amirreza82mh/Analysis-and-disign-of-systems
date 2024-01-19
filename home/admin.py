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


class AdminContact(admin.ModelAdmin):
    list_display=[
        'first_last_name',
    ]

admin.site.register(models.Contact, AdminContact)


class AdminSanse(admin.ModelAdmin):
    list_display=[
        'ticket'
    ]

admin.site.register(models.Sanse_Viewer, AdminSanse)


class AdminAEC(admin.ModelAdmin):
    list_display=[
        'exhibition',
        'artwork',
        'curator',
    ]
admin.site.register(models.Artwork_Exhibition_Curator, AdminAEC)


admin.site.register(models.Sans)