"""
Main URL configuration for the OC Lettings Site project.

This module defines the root URL configuration for the entire project,
including routing to sub-applications and custom error handlers.
It serves as the central hub for all URL routing in the application.

URL Patterns:
    '': Home page view
    'lettings/': Include all lettings app URLs with namespace
    'profiles/': Include all profiles app URLs with namespace
    'admin/': Django admin interface

Custom Error Handlers:
    handler404: Custom 404 (Not Found) error page
    handler500: Custom 500 (Internal Server Error) error page
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

# Serve media and static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Custom error handlers for production use
handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'
handler403 = 'oc_lettings_site.views.custom_403'
