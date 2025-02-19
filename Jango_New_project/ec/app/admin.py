from django.contrib import admin
from app.models import product,Customer,Cart


# Register your models here.
@admin.register(product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','discounted_price',"category","product_image"]
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
     list_display =['id','user','locality',"city","state","zipcode"]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
     list_display = ['id','user','product','quantity']
