from django.contrib import admin
from . models import WatchList, WatchCategory, Reviews

admin.site.register(WatchList)
admin.site.register(WatchCategory)
admin.site.register(Reviews)