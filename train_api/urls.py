from .views import TrainViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'train', TrainViewSet, basename='train')
urlpatterns = router.urls
