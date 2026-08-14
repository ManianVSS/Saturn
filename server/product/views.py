from django.shortcuts import render

from core.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, exact_fields_filter_lookups, ServerOrgGroupObjectLevelPermission, \
    ServerOrgGroupViewSet, datetime_fields_filter_lookups, compare_fields_filter_lookups, enum_fields_filter_lookups, \
    org_model_view_set_filterset_fields, org_model_ordering_fields
from .models import Attachment, Product, ProductConfig
from .serializers import ProductAttachmentSerializer, ProductSerializer, ProductConfigSerializer


class ProductAttachmentViewSet(ServerOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = ProductAttachmentSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ProductViewSet(ServerOrgGroupViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ProductConfigViewSet(ServerOrgGroupViewSet):
    queryset = ProductConfig.objects.all()
    serializer_class = ProductConfigSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['product', 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'product': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'properties': compare_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)