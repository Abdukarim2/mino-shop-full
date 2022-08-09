from django.contrib import admin
from .models import Category, Color, Size, Material, Product
from django.utils.html import mark_safe


@admin.register(Category)
class CategoryAdminRegister(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdminRegister(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Color)
class ColorAdminRegister(admin.ModelAdmin):
    list_display = ['name', 'color']

    def color(self, obj):
        html = f"""
                <div style="width:25px; height:25px; background-color:{obj.name}; border:1px solid black; background"></div>
                """
        return mark_safe(html)

    color.short_description = "Rang"


admin.site.register(Size)

admin.site.register(Material)
