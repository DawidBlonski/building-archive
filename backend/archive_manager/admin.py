from django.contrib import admin
from .models import PostCode,City,Street,AddresPoint,Buildings

@admin.register(PostCode,City,Street,AddresPoint,Buildings)
class AuthorAdmin(admin.ModelAdmin):
    pass

