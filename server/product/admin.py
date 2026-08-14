from django.contrib import admin

from core.admin import CustomModelAdmin, org_model_list_filter_base
from .models import Attachment, Product, ProductConfig


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = org_model_list_filter_base + ( )
    # display_order = 1


@admin.register(Product)
class ProductAdmin(CustomModelAdmin):
    search_fields = ['name', 'summary', 'description', ]
    list_filter = org_model_list_filter_base + ( )
    display_order = 1


@admin.register(ProductConfig)
class ProductConfigAdmin(CustomModelAdmin):
    search_fields = ['name', 'summary', 'description', ]
    list_filter = org_model_list_filter_base + ( )
    display_order = 2