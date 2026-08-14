from django.db import models
from django_yaml_field import YAMLField

from core.models import OrgGroup, OrgModel, NotMutablePublishOrgModel
from core.storage import CustomFileSystemStorage

class Attachment(OrgModel):
    name = models.CharField(max_length=256)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='product', blank=False, null=False)


class Product(OrgModel):
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class ProductConfig(OrgModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='configs')
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    properties = YAMLField(null=True, blank=True)


model_name_map ={
    'Attachment': Attachment,
    'Product': Product,
    'ProductConfig  ': ProductConfig,    
}
