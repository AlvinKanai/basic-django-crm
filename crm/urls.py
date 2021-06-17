from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
