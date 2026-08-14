from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from core.admin import CustomModelAdmin, org_model_list_filter_base
from .models import ApplicationType, Application, Release, ArtifactType, Artifact, DocumentType, Document


@admin.register(ApplicationType)
class ApplicationTypeAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 1


@admin.register(Application)
class ApplicationAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('application_type', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 2


@admin.register(Release)
class ReleaseAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('application', RelatedOnlyFieldListFilter),
        'date',
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 3


@admin.register(ArtifactType)
class ArtifactTypeAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 4


@admin.register(Artifact)
class ArtifactAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('release', RelatedOnlyFieldListFilter),
        ('artifact_type', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'link', 'file', ]
    display_order = 5


@admin.register(DocumentType)
class DocumentTypeAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 6


@admin.register(Document)
class DocumentAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('release', RelatedOnlyFieldListFilter),
        ('document_type', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'link', 'file', ]
    display_order = 7
