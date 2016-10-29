from django.contrib import admin

from .models import Category, Cutter, Seller, Url_in_Seller

admin.site.register(Seller)
admin.site.register(Url_in_Seller)
admin.site.register(Category)
admin.site.register(Cutter)
