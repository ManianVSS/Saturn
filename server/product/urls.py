from django.urls import include, path
from rest_framework import routers

from .views import ProductAttachmentViewSet, ProductViewSet, ProductConfigViewSet

router = routers.DefaultRouter()

router.register(r'product_attachments', ProductAttachmentViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_configs', ProductConfigViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
