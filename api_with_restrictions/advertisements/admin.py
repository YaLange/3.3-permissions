from django.contrib import admin

from advertisements.models import Advertisement, AdvertisementFavorites


@admin.register(Advertisement)
class AdminAdvertisement(admin.ModelAdmin):
    list_display = ['id', 'title', 'draft', 'status', 'creator', 'created_at', 'updated_at']
    list_editable = ['title', 'draft', 'status', 'creator']

@admin.register(AdvertisementFavorites)
class AdminAdvertisementFavorites(admin.ModelAdmin):
    list_display = ['id', 'user']
