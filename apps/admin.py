from django.contrib import admin
from apps.models import Car, Brand


@admin.register(Car)
class CarAdmin(admin.ModelAdmin): 
    list_display = ('id', 'model', 'year', 'price', 'brand')
    list_display_links = ('id', 'model')
    search_fields = ('id', 'model', 'brand')
    list_filter = ('year', 'brand')
    ordering = ['-id',]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')