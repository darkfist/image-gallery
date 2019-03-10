from django.contrib import admin

from .models import Image, ImageUpload

admin.site.register(Image)
admin.site.register(ImageUpload)