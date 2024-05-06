from django.contrib import admin
from .models import Product, Category, Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'slug']
    #используется для того, что- бы указывать поля, значение которых устанавливается автоматически
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']

