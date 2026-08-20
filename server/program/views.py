from core.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, datetime_fields_filter_lookups, exact_fields_filter_lookups, \
    ServerOrgGroupObjectLevelPermission, ServerOrgGroupViewSet, org_model_view_set_filterset_fields, \
    org_model_ordering_fields, date_fields_filter_lookups, compare_fields_filter_lookups, enum_fields_filter_lookups
from .models import ApplicationType, Application, Release, ArtifactType, DocumentType, Artifact, Document, \
                    Attachment, Tag, ProgramIncrement, Epic, Feature, Sprint, Story
from .serializers import ApplicationTypeSerializer, ApplicationSerializer, ProgramReleaseSerializer, \
    ArtifactTypeSerializer, DocumentTypeSerializer, ArtifactSerializer, DocumentSerializer, \
    ProgramAttachmentSerializer, ProgramTagSerializer, ProgramIncrementSerializer, EpicSerializer, \
    ProgramFeatureSerializer, SprintSerializer, StorySerializer


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


class ProgramAttachmentViewSet(ServerOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = ProgramAttachmentSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ProgramTagViewSet(ServerOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = ProgramTagSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ProgramIncrementViewSet(ServerOrgGroupViewSet):
    queryset = ProgramIncrement.objects.all()
    serializer_class = ProgramIncrementSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class EpicViewSet(ServerOrgGroupViewSet):
    queryset = Epic.objects.all()
    serializer_class = EpicSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'weight', 'pi', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'pi': fk_fields_filter_lookups,
        'pi__name': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,        
    }.update(org_model_view_set_filterset_fields)


class ProgramFeatureViewSet(ServerOrgGroupViewSet):
    queryset = Feature.objects.all()
    serializer_class = ProgramFeatureSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'weight', 'epic', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'pi': fk_fields_filter_lookups,
        'pi__name': string_fields_filter_lookups,
        'epic': fk_fields_filter_lookups,
        'epic__name': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,        
    }.update(org_model_view_set_filterset_fields)


class SprintViewSet(ServerOrgGroupViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'pi', 'start_date', 'end_date', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {        
        'pi': fk_fields_filter_lookups,
        'pi__name': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class StoryViewSet(ServerOrgGroupViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [ServerOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'weight', 'rank', 'sprint', 'feature', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'sprint': fk_fields_filter_lookups,
        'sprint__name': string_fields_filter_lookups,
        'feature': fk_fields_filter_lookups,
        'feature__name': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'rank': compare_fields_filter_lookups,        
    }.update(org_model_view_set_filterset_fields)