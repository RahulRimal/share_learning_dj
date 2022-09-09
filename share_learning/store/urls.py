from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()

router.register('customers', views.CustomerViewSet)
router.register('posts', views.PostViewSet, basename='posts')

urlpatterns = router.urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('store.urls')),
# ]