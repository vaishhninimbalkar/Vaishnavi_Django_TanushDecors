from django.contrib import admin
from .models import CartItem, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'pub_date', 'was_published_recently')
    list_filter = ('category', 'pub_date')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)