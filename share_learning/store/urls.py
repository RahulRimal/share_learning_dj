from cgitb import lookup
from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()

router.register('customers', views.CustomerViewSet)
router.register('posts', views.PostViewSet, basename='posts')

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('images', views.PostImageViewSet, basename='post-images')

urlpatterns = router.urls + posts_router.urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('store.urls')),
# ]
