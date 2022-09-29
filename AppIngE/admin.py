from django.contrib import admin
from .models import *

# Posteos
class PosteoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
admin.site.register(Posteo,PosteoAdmin)
# Avatar
admin.site.register(Avatar)
