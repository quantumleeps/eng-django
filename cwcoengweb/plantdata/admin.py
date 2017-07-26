from django.contrib import admin

from .models import Location, Group, Point

# Register your models here.

admin.site.register(Location)
admin.site.register(Group)
admin.site.register(Point)