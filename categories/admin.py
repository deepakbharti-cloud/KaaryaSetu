from django.contrib import admin
from .models import Category, SubCategory


class SubCategoryInline(admin.TabularInline):
    # Admin panel mein Category ke andar hi subcategories add kar sakte hain
    model = SubCategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
