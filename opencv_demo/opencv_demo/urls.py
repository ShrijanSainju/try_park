from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # ✅ include added

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('processor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
