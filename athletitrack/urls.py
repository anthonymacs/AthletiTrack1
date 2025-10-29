#athletitrack/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views 
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.views.static import serve as static_serve


urlpatterns = [

    path('', core_views.dashboard, name='dashboard'),

    path('admin/', admin.site.urls),

    path('accounts/', include('users.urls')), # For our signup page
    path('accounts/', include('django.contrib.auth.urls')), # For login, logout etc.

    path('athletes/', include('athletes.urls')),  # Add this line
    path('events/', include('events.urls')),
    path('reports/', include('reports.urls')), # Add this line
    path('core/', include('core.urls')), # Add this if not already present

    path('coaches/', include('coaches.urls')), # Add this line

    path('organization/', include('organization.urls')),

    path('', include('pwa.urls')),

    path(
        "service-worker.js",
        never_cache(lambda request: static_serve(
            request, "service-worker.js", document_root=settings.STATIC_ROOT
        )),
        name="service-worker.js",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
