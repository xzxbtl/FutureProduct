from django.contrib import admin

from .models import Products, NotesUser


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(NotesUser)
