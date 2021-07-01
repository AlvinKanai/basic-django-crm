from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('cocrm/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('categories/',include('categories.urls', namespace='categories')),
    path('reset-password/', PasswordResetView.as_view(), name = 'reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
