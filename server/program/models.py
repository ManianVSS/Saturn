from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import OrgModel, NotMutablePublishOrgModel
from core.storage import CustomFileSystemStorage
from server.settings import MEDIA_BASE_NAME

class ApplicationType(NotMutablePublishOrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Application(NotMutablePublishOrgModel):
    application_type = models.ForeignKey(ApplicationType, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='applications')
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Release(NotMutablePublishOrgModel):
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='releases')
    name = models.CharField(max_length=256, )
    version = models.CharField(max_length=256)
    date = models.DateTimeField()
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    release_notes = models.FileField(storage=CustomFileSystemStorage, upload_to='program', blank=True, null=True,
                                     verbose_name='Release notes file')


class ArtifactType(NotMutablePublishOrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Artifact(NotMutablePublishOrgModel):
    release = models.ForeignKey(Release, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='artifacts')
    artifact_type = models.ForeignKey(ArtifactType, on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='artifacts')
    name = models.CharField(max_length=256)
    link = models.TextField(null=True, blank=True)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='program', blank=True, null=True, )
    checksum = models.TextField(null=True, blank=True)


class DocumentType(NotMutablePublishOrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Document(NotMutablePublishOrgModel):
    release = models.ForeignKey(Release, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='documents')
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='documents')
    name = models.CharField(max_length=256)
    link = models.TextField(null=True, blank=True)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='program', blank=True, null=True, )
    checksum = models.TextField(null=True, blank=True)



class Attachment(OrgModel):
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to=MEDIA_BASE_NAME, blank=False,
                            null=False)


class Tag(OrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class ProgramStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft'),
    IN_PROGRESS = 'IN_PROGRESS', _('In progress'),    
    COMPLETED = 'COMPLETED', _('Completed'),
    ACCEPTED = 'ACCEPTED', _('Accepted'),


class ProgramIncrement(OrgModel):
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')


class Epic(OrgModel):
    pi = models.ForeignKey(ProgramIncrement, null=True, on_delete=models.SET_NULL, related_name='epics')
    name = models.CharField(max_length=256)
    status = models.CharField(max_length=20, choices=ProgramStatus.choices, default=ProgramStatus.DRAFT)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='epic_attachments', blank=True)


class Feature(OrgModel):
    pi = models.ForeignKey(ProgramIncrement, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='features')
    epic = models.ForeignKey(Epic, null=True, on_delete=models.SET_NULL, related_name='features')
    name = models.CharField(max_length=256)
    status = models.CharField(max_length=20, choices=ProgramStatus.choices, default=ProgramStatus.DRAFT)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='feature_attachments', blank=True)


class Sprint(OrgModel):
    pi = models.ForeignKey(ProgramIncrement, null=True, blank=True, on_delete=models.SET_NULL,
                           related_name='sprints')
    name = models.CharField(max_length=256)
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')

    def __str__(self):
        return "Sprint-" + str(self.name) + " for release " + str(self.pi.name if self.pi else "<unset>")


class Story(OrgModel):
    class Meta:
        verbose_name_plural = "stories"

    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True)
    feature = models.ForeignKey(Feature, null=True, on_delete=models.SET_NULL, related_name='stories')
    name = models.CharField(max_length=256, )
    status = models.CharField(max_length=20, choices=ProgramStatus.choices, default=ProgramStatus.DRAFT)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, related_name='story_attachments', blank=True)
    rank = models.IntegerField()


model_name_map = {
    'ApplicationType': ApplicationType,
    'Application': Application,
    'Release': Release,
    'ArtifactType': ArtifactType,
    'Artifact': Artifact,
    'DocumentType': DocumentType,
    'Document': Document,

    'Attachment': Attachment,
    'Tag': Tag,
    'ProgramIncrement': ProgramIncrement,
    'Epic': Epic,
    'Feature': Feature,
    'Sprint': Sprint,
    'Story': Story,
}
