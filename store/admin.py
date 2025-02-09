from django.contrib import admin
from .models import Product,Variation
# Register your models here.
class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name','price','stock','category','created_date','is_available')
    
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value','is_active')

admin.site.register(Product,productAdmin)
admin.site.register(Variation,VariationAdmin)