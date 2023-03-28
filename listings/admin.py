from django.contrib import admin
from listings.models import Listing, Poi
from .forms import PoiForm

# Register your models here - so that model can be seen on admin site


class PoiAdmin(admin.ModelAdmin):
    form = PoiForm

admin.site.register(Listing)
admin.site.register(Poi, PoiAdmin)
