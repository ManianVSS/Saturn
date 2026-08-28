from core.models import base_model_base_fields, org_model_base_fields
from core.serializers import ServerModelSerializer
from .models import Attachment, Site, Engineer, EngineerOrgGroupParticipation, SiteHoliday, Leave

class PeopleAttachmentSerializer(ServerModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class SiteSerializer(ServerModelSerializer):    
    class Meta:
        model = Site
        fields = org_model_base_fields + ['name', 'summary', 'attachments', ]


class EngineerSerializer(ServerModelSerializer):
    class Meta:
        model = Engineer
        fields = org_model_base_fields + ['employee_id', 'name', 'auth_user', 'role', 'site', 'points', 'attachments', ]


class EngineerOrgGroupParticipationSerializer(ServerModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipation
        fields = org_model_base_fields + ['engineer', 'role', 'capacity', ]


class SiteHolidaySerializer(ServerModelSerializer):
    class Meta:
        model = SiteHoliday
        fields = base_model_base_fields + ['name', 'date', 'summary', 'attachments', 'site', ]


class LeaveSerializer(ServerModelSerializer):
    class Meta:
        model = Leave
        fields = base_model_base_fields + ['engineer', 'start_date', 'end_date', 'summary', 'attachments', 'status', ]


serializer_map = {
    Attachment: PeopleAttachmentSerializer,
    Site: SiteSerializer,
    Engineer: EngineerSerializer,
    EngineerOrgGroupParticipation: EngineerOrgGroupParticipationSerializer,
    SiteHoliday: SiteHolidaySerializer,
    Leave: LeaveSerializer,
}
