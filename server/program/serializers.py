from core.models import org_model_base_fields
from core.serializers import ServerModelSerializer
from .models import ApplicationType, Application, Release, ArtifactType, Artifact, DocumentType, Document, \
                    Attachment, Tag, ProgramIncrement, Story, Sprint, Feature, Epic


class ApplicationTypeSerializer(ServerModelSerializer):
    class Meta:
        model = ApplicationType
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ApplicationSerializer(ServerModelSerializer):
    class Meta:
        model = Application
        fields = org_model_base_fields + ['application_type', 'name', 'summary', 'description', ]


class ProgramReleaseSerializer(ServerModelSerializer):
    class Meta:
        model = Release
        fields = org_model_base_fields + ['application', 'name', 'version', 'date', 'summary', 'description',
                                          'release_notes', ]


class ArtifactTypeSerializer(ServerModelSerializer):
    class Meta:
        model = ArtifactType
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ArtifactSerializer(ServerModelSerializer):
    class Meta:
        model = Artifact
        fields = org_model_base_fields + ['release', 'artifact_type', 'name', 'link', 'file', 'checksum', ]


class DocumentTypeSerializer(ServerModelSerializer):
    class Meta:
        model = DocumentType
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class DocumentSerializer(ServerModelSerializer):
    class Meta:
        model = Document
        fields = org_model_base_fields + ['release', 'document_type', 'name', 'link', 'file', 'checksum', ]



class ProgramAttachmentSerializer(ServerModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class ProgramTagSerializer(ServerModelSerializer):
    class Meta:
        model = Tag
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ProgramIncrementSerializer(ServerModelSerializer):
    class Meta:
        model = ProgramIncrement
        fields = org_model_base_fields + ['name', 'summary', 'description', 'start_date', 'end_date', ]


class EpicSerializer(ServerModelSerializer):
    # Don't need declare serializer for relationss as ServerModelSerializer takes care of that
    # Commented: attachments = ProgramAttachmentSerializer(many=True, read_only=True)
    class Meta:
        model = Epic
        fields = org_model_base_fields + ['pi', 'name', 'status', 'summary', 'description', 'weight', 'attachments', ]


class ProgramFeatureSerializer(ServerModelSerializer):
    class Meta:
        model = Feature
        fields = org_model_base_fields + ['pi', 'epic', 'name', 'status', 'summary', 'description', 'weight', 'attachments', ]


class SprintSerializer(ServerModelSerializer):
    class Meta:
        model = Sprint
        fields = org_model_base_fields + ['pi', 'name', 'start_date', 'end_date', ]


class StorySerializer(ServerModelSerializer):    
    class Meta:
        model = Story
        fields = org_model_base_fields + ['sprint', 'feature', 'name', 'status', 'summary', 'description', 'weight', 'attachments', 'rank', ]



serializer_map = {
    ApplicationType: ApplicationTypeSerializer,
    Application: ApplicationSerializer,
    Release: ProgramReleaseSerializer,
    ArtifactType: ApplicationTypeSerializer,
    Artifact: ArtifactSerializer,
    DocumentType: DocumentTypeSerializer,
    Document: DocumentSerializer,

    Attachment: ProgramAttachmentSerializer,
    Tag: ProgramTagSerializer,
    ProgramIncrement: ProgramIncrementSerializer,
    Epic: EpicSerializer,
    Feature: ProgramFeatureSerializer,
    Sprint: SprintSerializer,
    Story: StorySerializer,
}
