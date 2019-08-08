#!/usr/bin/env python
from django.contrib import admin
from .models import MyShop
from .models import Type, Category, SubCategory
# Register your model here.


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'price', 'image', 'specifications', 'about',
                    'create_time', 'update_time', 'type', 'category', 'sub_category')
    list_display_links = ('title', 'product', 'type', 'sub_category')
    search_fields = ('product', 'category', 'subcategory', 'update_time', 'specifications')


admin.site.register(MyShop, BdAdmin)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(SubCategory)
# admin.site.register(Rubric)
