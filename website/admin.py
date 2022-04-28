from django.contrib import admin
from .models import Category, Object, ImageHome, Trip, Equipment, Published, Links
from django.utils.safestring import mark_safe

admin.site.site_header = 'Astrofotografía Austral'


class ImageHomeAdm(admin.ModelAdmin):
    list_display = ['caption', 'rating']
    readonly_fields = ["preview_image"]

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.imagehome.url,
            width=obj.imagehome.width,
            height=obj.imagehome.height,
        )
        )


class ObjectAdm(admin.ModelAdmin):
    search_fields = ['Name']
    list_filter = ['category']
    list_display = ['Name', 'category']
    # Aca va el campo con el nombre dle metodo de abajo
    readonly_fields = ["preview_image"]

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image1.url,
            width=obj.image1.width,
            height=obj.image1.height,
        )
        )


class CategoryAdm(admin.ModelAdmin):
    #    list_display = ['title', 'preview_image']
    # Para hacer el Preview de la Imagen. Metodo abajo

    readonly_fields = ["preview_image", "slug"]  # Metodo definido abajo

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.HeaderImage.url,
            width=obj.HeaderImage.width,
            height=obj.HeaderImage.height,
        )
        )


class TripAdm(admin.ModelAdmin):
    # Para hacer el Preview de la Imagen. Metodo abajo
    list_display = ['name', 'date_trip']
    readonly_fields = ["preview_image", ]  # Metodo definido abajo

    @admin.display(ordering='date_trip')
    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )


class EquipmentAdm(admin.ModelAdmin):
    # Para hacer el Preview de la Imagen. Metodo abajo
    list_display = ['name']
    readonly_fields = ["preview_image", ]  # Metodo definido abajo

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )


class PublishedAdm(admin.ModelAdmin):
    # Para hacer el Preview de la Imagen. Metodo abajo
    list_display = ['name']
    readonly_fields = ["preview_image", ]  # Metodo definido abajo

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )


    # Register your models here.
admin.site.register(Category, CategoryAdm)
admin.site.register(Object, ObjectAdm)
admin.site.register(ImageHome, ImageHomeAdm)
admin.site.register(Trip, TripAdm)
admin.site.register(Equipment, EquipmentAdm)
admin.site.register(Published, PublishedAdm)
admin.site.register(Links)
