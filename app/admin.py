from django.contrib import admin

from app.models import Products, Testimony, ShopItem, Team, Blog, SiteDescription, Contact

# Register your models here.

admin.site.register(Products)
admin.site.register(Testimony)
admin.site.register(ShopItem)
admin.site.register(Team)
admin.site.register(Blog)
admin.site.register(SiteDescription)
admin.site.register(Contact)


