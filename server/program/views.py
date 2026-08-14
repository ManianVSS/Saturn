from core.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, datetime_fields_filter_lookups, exact_fields_filter_lookups, \
    ServerOrgGroupObjectLevelPermission, ServerOrgGroupViewSet, org_model_view_set_filterset_fields, \
    org_model_ordering_fields
from .models import ApplicationType, Application, Release, ArtifactType, DocumentType, Artifact, Document
from .serializers import ApplicationTypeSerializer, ApplicationSerializer, ProgramReleaseSerializer, \
    ArtifactTypeSerializer, \
    DocumentTypeSerializer, ArtifactSerializer, DocumentSerializer


class ProgramApplicationTypeViewSet(ServerOrgGroupViewSet):
    queryset = ApplicationType.objects.all()
    serializer_class = ApplicationTypeSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = [ 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ProgramApplicationViewSet(ServerOrgGroupViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = [ 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'application_type': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ProgramReleaseViewSet(ServerOrgGroupViewSet):
    queryset = Release.objects.all()
    serializer_class = ProgramReleaseSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = [ 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'application': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'version': string_fields_filter_lookups,
        'date': datetime_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ArtifactTypeViewSet(ServerOrgGroupViewSet):
    queryset = ArtifactType.objects.all()
    serializer_class = ArtifactTypeSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = [ 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ArtifactViewSet(ServerOrgGroupViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = ['name', 'link', 'file', ]
    ordering_fields = [ 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'release': fk_fields_filter_lookups,
        'artifact_type': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class DocumentTypeViewSet(ServerOrgGroupViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = [ 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class DocumentViewSet(ServerOrgGroupViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = ['name', 'link', 'file', ]
    ordering_fields = [ 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'release': fk_fields_filter_lookups,
        'document_type': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)
