from core.models import org_model_base_fields
from core.serializers import ServerModelSerializer
from .models import Attachment, Product, ProductConfig

class ProductAttachmentSerializer(ServerModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class ProductSerializer(ServerModelSerializer):
    class Meta:
        model = Product
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ProductConfigSerializer(ServerModelSerializer):
    class Meta:
        model = ProductConfig
        fields = org_model_base_fields + ['product', 'name', 'summary', 'description', 'properties', ]


serializer_map = {
    Attachment: ProductAttachmentSerializer,
    Product: ProductSerializer,
    ProductConfig: ProductConfigSerializer,
}
