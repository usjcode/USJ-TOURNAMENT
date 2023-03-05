
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Tournaments.urls')),
    path('staff/',include('staff.urls')),
    path('candidate/',include('candidate.urls'))
    
]

# server config
if not settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    