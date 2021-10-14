from rest_framework.routers import DefaultRouter
from rabbit.views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)