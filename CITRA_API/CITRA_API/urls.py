from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from CITRApp.views import UserViewSet

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
